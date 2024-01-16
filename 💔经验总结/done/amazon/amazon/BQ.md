
# words:

pull out effort
map out key frame
drive forward
swim upstream



# LP:

https://www.carrus.io/blog/amazon-newprinciples

invent and simplify, customer obsession, ownership,
delivery result, dive deep, Insist on the Highest Standards

definition, vision

This role requires the desire to innovate, design, and build the framework and tools that will enable developers to deliver the best music experience for millions of customers around the world. You’ll also be coaching other engineers, developing engineering and operational processes, and encouraging excellence within the team.

a growing team that is passionate about experimenting and innovating for customers, has a demonstrable track record of success in delivering new features and products, and is excited about having end-to-end ownership of high-impact, high-visibility projects. 

 evaluating alternative solutions,
(with both business and technical partners) are absolute requirements. 


#1: Customer Obsession
-  focus on breaking trade-off conditions, and providing an extraordinary experience to wow our loyal customers. seek customer feedbacks
 1. feedback tool
 2. meeting with PM and collect pain points
 3. analysing global customer and get more favor of survey and data results
 4. knowledge sharing 


- We obsess about building robust and scalable system for our consumers and pivot off of understanding problems before building solutions. I was fortunate to build

high available, resilient, high throughput data serving platform.


#2: Ownership

- automation

- third party validation
 1. UK different timezone, service not responding
 2. diagnoze issue

#3: Invent and Simplify

- Debug runbook
 1. simplify process, extract logs and auto fetch for co-relation id, fetch work done to similar problem and append to alert
 2. oncall retro-spec 

P: I use both quantitative and qualitative methods to find out what my customers need. [I kept one sentence of the general stuff as a lead in – you could use more, but don’t ramble on.] For example, last month I wanted to find out what type of content was most popular on our site so we could do more of it.

A: I looked at data on my top customers, in terms of the customers most engaged on my platform, and I could see that content about IT certification is very popular. So I started to talk to customers about the role of certification in their workplace. It turns out that getting certified is important because it’s tied to getting promoted. As a result we started doing online trainings for the certifications. So instead of just a course or video, we do live trainings now as part of the educational product line up.


R: 

#4: Are Right, A Lot
#5: Hire and Develop the Best
creating clear, focused, measurable goals. 


#6: Insist on the Highest Standards

 HYPOTHESIS editing their order post-purchase 
 Other fulfillment types including but not limited to shipping, unscheduled pickup, express delivery do not currently support this feature. In FY23, 36.0%1 of total orders have been amended. Among the amended orders, 85.8%1 has new item added, 56.7%1 has quantity of existing items incremented, and 4.1%1 has quantity of existing items decremented. On average, 4.71 new items are added, 1.11 existing items are incremented and 1.31 existing items are decremented. Historically, 62%2 of the amendment happen in the first 30 minutes when an order is placed at the time when slot time is less than 24 hours away and 80%2 of the amendment happen in the last 24 hours when an order is placed at the time when slot time is more than 24 hours away. 69%2 of the amendment happens between 6pm and 12am. See Product Requirement section for feature parity comparison between TTS and the website/app today.

 THEN we will help our customers manage their open order more seamlessly,

 RESULTING in an increase in customer engagement.


- performance improvement
 web-vitals evaluate critical user-centric outcome.
 content paint, cumulative layout shift
![]()



#7: Think Big

error logging extraction and alert
 - splunk like error: action, message, query, latency, errors, tag info, platform
 - modes available for further fine-tune: status, timechart, verbose mode
 - 


permission/rule, saw big opportunity, delta in plan: , seek consultation to really understand long term plan, bigger opportunity and opportunity
- prefetch
- end to end flow
- performance panalty
- weigh in time constraint
- result: 
- data & metric: 
https://dgraph.io/blog/post/how-does-graphql-subscription/

#8: Bias for Action

allow engineers to work effectively


 
own the part when main stackholder is not availble, signup myself for upcoming demo and update on codebase after user acceptance 
with consulting with the previous stackholder, step up to move forward with calculated risks and eta.




#9: Frugality




#10: Learn and Be Curious

learn react native


learn ML

#11 Earn Trust

 trust with PM
 - newly onboard projects


good communicator
drive consensus between multiple teams to deliver result effectively
 

#12: Dive Deep
# assumption/goal setting, data, insight

identify every single element of a project, but there’s a lot of value in spending time thinking through the externalities and issues related to a project. This role requires you to have a good sense of the overall architecture of your systems and a solid understanding of how to design complex software. It probably also requires you to be able to understand business requirements and translate them into software. 


#13: Have Backbone; Disagree and Commit



#14: Deliver Results

notify customer we are solving
tight timeline
get awareness of software release

think creatively 
update and rollout gradually with oncall engineers

huge decrease in bug report


obstacles?






#15:  Strive to Be Earth’s Best Employer
#16: Success and Scale Bring Broad Responsibility







---



provide infrastructure services, tools, and frameworks for all domain customers to increase productivity and throughput. In detail, the service platform includes 4 sub-teams: 

Messaging Platform 
- Internal Messaging (PB per day): Managed Kafka Service, Canal Service (MySQL to Kafka), Roller Service (In-house product: Kafka to S3/ElasticSearch/HDFS) 
- External Messaging (Millions of messages per day): Customer Communication Service for both transactional and marketing notifications including SMS, Email, iOS Push, Android Push, KaKao, and Line. 

Weblogging Platform 
- A centralized logging platform (1k data types and trillion events) to track and analyze customers' journeys in Coupang. It provides both a Hive interface for business analysts/data scientists to build data insights. It also provides a real-time event interface for ML feature generation in the search and discovery domain. 

Common Frameworks and Tools 
- This team provides a centralized deployment system, AWS resources and cost management system, A global API Gateway (Internal & Public) 

Common Data Service  
- Provided an aggregated catalog view (180+ columns) using Cassandra, Redis and Spark to merge multiple data sources.



 real-time data pipeline solution.


Weblogging product "Lumberjack" is a frontend logging tool to track and analyze customers' journeys in Coupang. It includes mobile libraries (iOS, Android, web) and a backend data aggregation engine. Domain teams can easily use Lumberjack to extract and aggregate the business metrics they need, such as product impressions, clicks, orders, and related CTR, conversion, etc.

A real-time data pipeline solution was standardized after several products we developed based on Kafka and Spark. I led the team to consolidate some common data processing patterns and deployment tools together to launch a Coupang in-house real-time data pipeline to help domain teams increase productivity. Specifically, if a customer needs to run a data processing job, they only need to clone our Github repository. They can implement the interface, fill in required AWS metadata, then a job can be deployed in less than one hour.