Clarify
Key Questions

How many elevators do we have, i.e. do we need to consider like elevator bank? 2 anwers we may get:
If only one elevator, just one elevator
Else, we will have List<Elevator> elevators = new ArrayList<>();
Do we need to consider the capacity/the weight limit of an elevator?
It should be fine, if we need to consider this, we just need to add checkCapacity() or and add alarm() methods in our elevator instance
Other Questions - The questions I encoutered while went through online, but I think probably it is not necessary and minor

What is the min floor and max floor of the elevator can move? (maybe because sometimes some levels are not reachable for some reason, like maintaince, or top-secrets floor, employee only)
Elevator Scheduling System
Also before going into OOD details, I want to spend some time about the "Elevator Scheduling System". I did went through many articles about this OOD design, but mostly they just directly go to the scheduling implementation, implicitly take some algorithms.

Elevator Scheduling System can be complicated, before I prepare this OOD, I thought all the elevators in the world has a very simple, common, best scheduling algorithm. However I found out that this is not the truth, there are many algorithms for it(Some ppl even mentioned it is a trade secret...). Based on https://cdmana.com/2021/02/20210202111024127g.html(equivalent Chinese version 中文版: https://cdmana.com/2021/02/20210202090419089B.htm), algorithms can be catogorized as below:

Traditional Algorithm

FCFS, , https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics), 其实就是FIFO的另外一种称呼
Elevator Algorithm/SCAN, https://en.wikipedia.org/wiki/Elevator_algorithm, 扫描算法
Look, https://en.wikipedia.org/wiki/LOOK_algorithm, 扫描算法的改进, 查找算法
SSTF, Shortest Seek First, https://en.wikipedia.org/wiki/Shortest_seek_first, 最短寻找楼层优先算法
Refer: http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf
Some resources in Chinese

就近响应
顺向截梯
参考知乎: https://www.zhihu.com/question/19747924
传统电梯派梯算法是就近响应或顺向截梯，效率不高。奥的斯采用的算法叫RSR，其逻辑原则是平均候梯时间最短。高级一点的人工智能算法会基于实时采集的流量数据，通过计算预测流量并进行相应的派梯。目前最先进的派梯系统是目标楼层型派梯，最早是迅达发明的，现在基本大厂商都有，其形式是乘客在大厅在终端输入设备上输入目标楼层，系统立即将派梯结果显示在该设备的显示屏上，乘客直接去指定的电梯前等候乘坐即可。
顺向截梯: https://zhidao.baidu.com/question/304817091.html
电梯顺向截梯是电梯的一个功能，比如电梯从1层向上，你在3层候梯。您选的是下方向，电梯内有人上8层，那么电梯不会相应您，要到8层，并且8层以上楼层没有呼梯后，换成下方向。经过3层时才会停梯接您。也就是说，乘客在本层呼梯。您的呼梯方向与电梯运行方向相同时，才会停梯相应。
参考: https://www.jianshu.com/p/6c0010a42c50
Realtime Scheduling Algorithms

PI(Priority Inversion)
FD-SCAN
Anyway, the conclusion is that there are many algorithms, no one is perfect, it is NP-Hard problem for 1 elevator without capacity constraint based on http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf(not sure for multiple and with capacity constraint, if it is still NP-Hard or not?) I have seen some dicussion saying that oh, this solution is not good blablabla because someone may wait for a long time blablabla...But I think it is fine, it is open-ended, should not be the key of OOD design. We can take the simple strategy, the elevator will first process UP requests where request floor is greater than current floor and then process Down requests where request floor is lower than current floor.

Core

Elevator
Button[] buttons // some solution does not have Button class, represents internal buttons, not including external?
Request, 针对是电梯的相对位置, 而不是针对人
InternalRequest
ExternalRequest
Controller
Controller
The best part I like is the Controller, which I only see in one of the solutions online. Most of the solutions either did not mention this part(they stop when they put external or internal requests to the queue or array). But it makes more sense to me to indicate how we really move the elevator, all the commands will be extecuted by the machinical device, right? So "Controller" will be used to represent the machine devide,

"Controller.goUp(int floor)" means elelvator goes up
"Controller.goUp(int floor)" means elelvator goes down
Skip User Cases Stage here
Simply say
Basic

Take Internal Requests
Take External Requests
Go Up
Go Down
I did not implement it, because

Open Gate
Close Gate
Optional

Check Capacity
Alarm if Capacity Exceeded
Code
I will not add getters and setters methods here for simplicity, and just image I have lombok configured here.
Note that we update upStops and downStops based on if elevetor should go up or down, not based on whether a person need to go up or down.(The implementation is definitely not 100% good or even correct, I might need to think about it more later..)

public enum Direction{
	UP,
	DOWN,
	STOPPED, // some solution does consider this and timeout for waiting passengers to come inside
	IDLE
}

public class Request{
	Type type;
	int floor;
	public Request(int floor){
		this.floor = floor;
	}
}

public class InternalRequest extends Request{
	public InternalRequest(int floor){
		super(floor);
		// type = Type.INSIDE;
	}
}

public class ExternalRequest extends Request{
	Direction direction;
	public ExternalRequest(int floor, Direction direction){
		super(floor);
		// type = Type.OUTSIDE; 
	}
}

public class Button{
	int floor;
	public Button(int floor){
		this.floor = floor;
	}
}

public class Elevator{
	public Status status;
	public int currentFloor;
	public boolean[] upStops;
	public boolean[] downStops;
	public int upStopsCount;
	public int downStopsCount;
	public Button[] buttons; // or List<Button> buttons
	public Controller controller;
	
	pubic Elevator(){
		direction = Direction.IDLE;
		currentFloor = 1;
		upStops = new boolean[n];
		downStops = new boolean[n];
		controller = new Controller(); 
		// deprecated
		// upRequests = new PriorityQueue<>((a, b) -> Integer.compare(a.floor, b.floor));
		// downRequests = new PriorityQueue<>((a, b) -> Integer.compare(b.floor, a.floor));
	}
	
	public void processUpRequest(){
		if(this.direction == Direction.IDLE) return;
		for(int i = this.currentFloor + 1; i < upStops.length; i++){
			if(upStops[i]){
				this.controller.goUp(i);
				openGate();
				closeGate();
			}
		}
		// all the left requests will be down requests
		// if none, the elevator is in idle state
		if(downRequestsCount == 0){
			this.direction = Direction.IDLE;
		}else{
			this.direction = Direction.DOWN;
		}
	}
	
	public void processDownRequest(){
		if(this.direction == Direction.IDLE) return;
		for(int i = this.currentFloor - 1; i >= 0; i--){
			if(downStops[i]){
				this.controller.goDown(i);
				openGate();
				closeGate();
			}
		}
		if(upRequestsCount == 0){
			this.direction = Direction.IDLE;
		}else{
			this.direction = Direction.UP;
		}
	}
	
	public void processButton(Button button){
		addRequest(new InternalRequest(button.floor));
	}
	
	// we update elevator's status when add request, or we can modify to add button design here, replace parameter from "request" to "button"
	public void addRequest(Request request){
		if(this.direction = Direction.UP){
			if(request.floor > this.currentFloor) {
				upStops[request.floor] = true;
				upStopsCount++;
			}
			else{
				downStops[request.floor] = true;
				downStopsCount++;
			}
		}else if(this.direction = Direction.DOWN){
			if(request.floor < this.currentFloor) {
				downStops[request.floor] = true;
				downStopsCount++;
			else {
				upStops[request.floor] = true;
				upStopsCount++;
			}
		} else{
			// if it is IDLE, then direction depends on current level and target level
			if(request.floor > this.currentFloor){
				upStops[request.floor] = true;
				upStopsCount++;
				this.direction = Direction.UP;
			}else{
				downStops[request.floor] = true;
				downStopsCount++;
				this.direction = Direction.DOWN;
			}
		}
	}
	
	public void openGate(Direction direction){
		this.controller.openGate();
		this.currentFloor = i;
		if(direction = Direction.UP){
		this.currentFloor = i;
			upStops[i] = false;
			upRequestsCount--;
		}else{
			downStops[i] = false;
			downRequestsCount--;
		}
		// wait for passengers to get in or out, e.g.
		this.controller.sleep(10); // sleep for 10 seconds
	}
	
	public void closeGate(){
		this.controller.closeGate();
	}
	
	public void start(){
		while(true){
			processUpRequests();
			processDownRequest();
		}
	}
}



class Elevator:
    _instance = None

    def __init__(self):
        self.currentFloor = 0

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with synchronized(cls):
                if cls._instance is None:
                    cls._instance = Elevator()
        return cls._instance