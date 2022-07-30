/*
Name: Abdul Moez Akbar
Date: 29th July'2022
This is the main driver class for the whole project. I have already included tests for the
functionality of this program in this main driver class. The tests check for legal values, illegal
values, and different methods of each class. All you have to do in run the driver class to display the output.
This program keeps track of all the registered vehicles within a province.
 */

package Assignment2;

// import package used in the class
import java.util.ArrayList;

/**
 * This class acts as the driver class for the whole project.
 * It acts as a collection class by creating an arrayList to keep track of all the
 * registered vehicles. Different methods are created to be used on the arrayList
 */
public class Registry {
    // declare fields
    private ArrayList<Vehicle> vehicleCollection = new ArrayList<Vehicle>();
    private int numVehicles;

    /**
     * This is the main function of the class that controls the flow of the program
     * @param args
     * @throws IllegalVehicle an exception class
     */
    public static void main(String[] args) throws IllegalVehicle {

        //create a registry object that can be used for all the vehicle objects
        Registry registry = new Registry();

        // legal values to be used in testing
        int year1 = 2015;
        int wheels1 = 4;
        String plateNumber1 = "ABCD123";
        int age1 = 20;
        int yearsDriving1 = 4;
        // object with legal values
        CarOwner owner1 = new CarOwner("moez",20,1234,2);

        // illegal values
        int year2 = 1850;
        int wheels2 = 1;
        String plateNumber2 = "123abcd";
        int age2 = -2;
        int yearsDriving2 = -3;


        try {
            // tells the user what is being tested
            System.out.println("This is a test to see if the getters and setters for Car class work.");
            System.out.println("There should be no exception thrown since all legal values are used.");


            // create a car object
            Car car1 = new Car(1234,owner1,1000,"car","abcd",
                    year1,wheels1,plateNumber1,4,true);
            // create a truck object
            Truck truck1 = new Truck(234,owner1,2000,"truck","honda",
                    year1,wheels1,plateNumber1,false,1000);
            //create a motorcycle object
            Motorcycle motorcycle1 = new Motorcycle(657,owner1,500,"honda","xyz",
                    year1,wheels1,plateNumber1);

            // add all the objects to the registry
            registry.addVehicle(car1);
            registry.addVehicle(truck1);
            registry.addVehicle(motorcycle1);


            System.out.println("Testing the getter functions shared by all the vehicles:");
            emptyLine();

            // a loop that iterates through the arrayList of vehicle objects
            for (int i = 0; i < registry.vehicleCollection.size(); i++){
                // display all the shared getter functions of each vehicle object in the array
                System.out.println("For " + registry.vehicleCollection.get(i).getClass().getSimpleName() +
                        " we have:");
                System.out.println("RegistrationNumber: " + registry.vehicleCollection.get(i).getRegistrationNumber());
                System.out.println("OdometerReading: " + registry.vehicleCollection.get(i).getOdometerReading());
                System.out.println("Make: " + registry.vehicleCollection.get(i).getMake());
                System.out.println("Model: " + registry.vehicleCollection.get(i).getModel());
                System.out.println("year: " + registry.vehicleCollection.get(i).getYear());
                System.out.println("numWheels: " + registry.vehicleCollection.get(i).getNumWheels());
                System.out.println("plateNumber: " + registry.vehicleCollection.get(i).getPlateNumber());
                emptyLine();
            }

            System.out.print("Now we are going to test if the averageMileage() and printRegistry() ");
            System.out.println("methods work for already created objects with legal values.");
            emptyLine();
            System.out.print("By calling the printRegistry() method, we should invoke ");
            System.out.println("the toString method of each vehicle in the registry:");

            // call the printRegistry() function to test it
            registry.printRegistry();
            emptyLine();

            System.out.println("Now we are testing the averageMileage function which should return 1166.6666:");
            // call the averageMileage function and set it equal to a variable
            float averageMileage = registry.averageMileage();
            // display the returned value
            System.out.println(averageMileage);


        } catch (IllegalVehicle e) { // if exception is thrown, catch it
            // display the excpetion message
            System.out.println(e.getMessage());
        }

        try {
            emptyLine();
            // tells the user what is being tested
            System.out.print("This is going to be a test to see if an exception is thrown if ");
            System.out.println("illegal year value is used:");
            // create a vehicle object with illegal year value
            Vehicle vehicle1 = new Vehicle(1234,owner1,1000,"abc","bcd",
                    year2,wheels1,plateNumber1);

        } catch (IllegalVehicle e) { // if an exception is thrown, catch it
            // display the exception message
            System.out.println(e.getMessage());
        }

        try {
            emptyLine();
            // tells the user what is being tested
            System.out.print("This is going to test if setting the mileage less than old value will");
            System.out.println(" throw an exception:");
            // create a vehicle object with legal values
            Vehicle vehicle2 = new Vehicle(1234,owner1,1000,"abc","bcd",
                    year1,wheels1,plateNumber1);
            // set the new value of mileage of vehicle to the same current value of mileage
            vehicle2.setOdometerReading(900);

        } catch (IllegalVehicle e){  // if exception is thrown, catch it
            // display the exception message
            System.out.println(e.getMessage());
        }

        try {
            emptyLine();
            // tells the user what is being tested
            System.out.print("This test will see if an exception is thrown if an illegal");
            System.out.println(" plate number value is put in:");
            // create a vehicle object with illegal plateNumber value
            Vehicle vehicle3 = new Vehicle(1234,owner1,1000,"abc","bcd",
                    year1,wheels1,plateNumber2);

        } catch (IllegalVehicle e) {  // if exception is thrown, catch it
            // display the exception message
            System.out.println(e.getMessage());
        }

        try {
            emptyLine();
            // tells the user what is being tested
            System.out.print("This test will see if an exception is thrown if an illegal value of ");
            System.out.println("numWheels is used: ");
            // create a vehicle object with illegal numWheels value
            Vehicle vehicle4 = new Vehicle(1234,owner1,1000,"abc","bcd",
                    year1,wheels2,plateNumber1);

        } catch (IllegalVehicle e) {  // if exception is thrown, catch it
            // display the exception message
            System.out.println(e.getMessage());
        }

        try {
            emptyLine();
            // tells the user what is being tested
            System.out.print("This test will see if an exception is thrown if an illegal value of ");
            System.out.println("age is used: ");
            // create a vehicle object with illegal age value
            CarOwner carowner2 = new CarOwner("moez",age2,123,4);

        } catch (IllegalVehicle e) {  // if exception is thrown, catch it
            // display the exception message
            System.out.println(e.getMessage());
        }

    }

    // getters

    /**
     * This is a getter for vehicleCollection
     * @return vehicleCollection
     */
    public ArrayList<Vehicle> getVehicleCollection() {
        return this.vehicleCollection;
    }

    /**
     * This is a getter for numVehicles
     * @return numVehicles
     */
    public int getNumVehicles() {
        numVehicles = vehicleCollection.size();
        return this.numVehicles;
    }

    // setters

    /**
     * This is a getter function for vehicleCollection
     * @param vehicleCollection an arrayList
     */
    public void setVehicleCollection(ArrayList<Vehicle> vehicleCollection) {
        this.vehicleCollection = vehicleCollection;
    }

    /**
     * This is a getter function for numVehucles
     * @param numVehicles a int
     */
    public void setNumVehicles(int numVehicles) {
        this.numVehicles = numVehicles;
    }

    /**
     * This function adds a vehicle object to an arrayList
     * @param vehicle an object
     */
    public void addVehicle(Vehicle vehicle) {
        vehicleCollection.add(vehicle);
    }

    /**
     * This function goes through all the vehicle objects in the arrayList and
     * invokes its toString method
     */
    public void printRegistry() {
        // a loop that iterates through each vehicle object in the arrayList
        for (Vehicle vehicle : vehicleCollection) {
            System.out.println(vehicle);
        }
    }

    /**
     * This function accesses the mileage of all the vehicle objects in the arrayList
     * and calculates the average mileage
     * @return averageMileage float
     */
    public float averageMileage() {
        // set up a float value to calculate sum of mileages
        float sum = 0;
        // set up a counter to count number of mileages in the arrayList
        int counter = 0;

        // a loop that iterates through all the vehicle objects in the arrayList
        for (Vehicle vehicle : vehicleCollection) {
            // access mileage using getter function and add it to the new arrayList
            sum += vehicle.getOdometerReading();
            counter += 1;
        }

        // divide sum by number of mileage values in the arrayList and return the result
        return (sum/counter);

    }

    /**
     * This function just prints an empty line for cleaner display of code
     */
    private static void emptyLine(){
        System.out.println();
    }
}
