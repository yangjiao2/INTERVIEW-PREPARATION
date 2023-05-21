import java.util.*;

class Solution {

  private static class Manager {  
    private static Manager manager;
    private static BooksDepartment booksDept;
    private static GeneralMerchandiseDepartment genMerchDept;
    private static FashionDepartment fashionDept;

    public static Manager getInstance() {
      manager = new Manager();
      booksDept = new BooksDepartment();
      booksDept.setName("Books department");
      genMerchDept = new GeneralMerchandiseDepartment();
        genMerchDept.setName("General Merchandise department");
      fashionDept = new FashionDepartment();
        fashionDept.setName("Fashion department");
      return manager;
    }

    public BooksDepartment getBookDepartment() { 
      return booksDept; 
    }
    public GeneralMerchandiseDepartment getGeneralMerchDepartment() { 
      return genMerchDept; 
    }
    public FashionDepartment getFashionMerchDepartment() { 
      return fashionDept; 
    }
    
    public void printInventory() {
      System.out.println("** All Inventory **");
      booksDept.printInventory();
      genMerchDept.printInventory();
      fashionDept.printInventory();
    }
    public void printBooksInventory() {
      booksDept.printInventory();
    }
    public void printGenMerchInventory() {
      genMerchDept.printInventory();
    }
    public void printFashionInventory() {
      fashionDept.printInventory();
    }
  }
    


  private static class Department {
    private final Map<String, Item> genInventory;
    private String genName;
    
    public Department() {
      genInventory = new HashMap<>();
    }

    public void setName(String name) {
      genName =  name;
    }
    
    public void add(Item item) { genInventory.putIfAbsent(item.getItemId(), item); }
    public void remove(Item item) { genInventory.remove(item.getItemId()); }
    public Item getItem(String itemId) { return genInventory.get(itemId); }
    public void printInventory() {
      System.out.println(genName);
      genInventory.values().stream().forEach(Item::print);
      System.out.println("\n");
    }
  }
  
  private static class BooksDepartment extends Department {
    private final Map<String, Item> bookInventory;
    
    public BooksDepartment() {
      bookInventory = new HashMap<>();
    }
  }
      
  private static class GeneralMerchandiseDepartment  extends Department {
    private final Map<String, Item> genMerchInventory;

    public GeneralMerchandiseDepartment() {
      genMerchInventory = new HashMap<>();
    }
  }
  
  private static class FashionDepartment extends Department  {
    private final Map<String, Item> fashionInventory;
    
    public FashionDepartment() {
      fashionInventory = new HashMap<>();
    }
  }
  
  private static class Item {
    private String itemId;
    private String name;
    private double price;
    private String description;
    private int quantity;

    public String getItemId() { return itemId; }
    public void setItemId(String itemId) { this.itemId = itemId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public int getQuantity() { return quantity; }
    public void setQuantity(int quantity) { this.quantity = quantity; }
    public void print() {
      System.out.print("Name: " + name + 
      ", Description: " + description + 
      ", Price: " + price + 
      ", Quantity: " + quantity + "");
    }
  }

  public static void main(String[] args) {
      Manager manager = Manager.getInstance();
      BooksDepartment bookDept = manager.getBookDepartment();
      GeneralMerchandiseDepartment genMerchDept = manager.getGeneralMerchDepartment();
      FashionDepartment fashionDept = manager.getFashionMerchDepartment();

      // Add a book
      Item book = new Item();
      book.setItemId("1");
      book.setName("To Kill a Mockingbird");
      book.setDescription("Required reading for Lit 101");
      book.setPrice(19.99);
      book.setQuantity(13);
      bookDept.add(book);

      // Add general merchandise
      Item runningShoes = new Item();
      runningShoes.setItemId("2");
      runningShoes.setName("Running Shoes");
      runningShoes.setDescription("Good for beach running");
      runningShoes.setPrice(89.99);
      runningShoes.setQuantity(7);
      genMerchDept.add(runningShoes);

      // TODO: Add Fashion Department
      Item cloth = new Item();
      cloth.setItemId("2");
      cloth.setName("Dress");
      cloth.setDescription("Good for party");
      cloth.setPrice(2209.99);
      cloth.setQuantity(3);
      fashionDept.add(cloth);
      
      // Print inventories
      manager.printBooksInventory();
      manager.printGenMerchInventory();
      manager.printInventory();
      manager.printFashionInventory();
  }
     
}
