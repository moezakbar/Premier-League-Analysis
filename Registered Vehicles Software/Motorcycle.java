/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This class is a subclass of the Vehicle class
 * it shares all the instances of its parent class
 */
public class Motorcycle extends Vehicle{

    /**
     * This is the constructor for the class
     * @param registrationNumber an int
     * @param owner an object
     * @param odometerReading an int
     * @param make a string
     * @param model a string
     * @param year an int
     * @param numWheels an int
     * @param plateNumber a int
     * @throws IllegalVehicle an exception class
     */
    public Motorcycle(int registrationNumber, CarOwner owner, int odometerReading, String make,
                      String model, int year, int numWheels, String plateNumber) throws IllegalVehicle{
        // call the constructor of the parent class
        super(registrationNumber, owner, odometerReading, make, model, year, numWheels, plateNumber);
    }

    /**
     * This function overrides the toString method of the parent class
     * @return s
     */
    public String toString() {
        String s = "This motorcycle is the " + this.getYear() + " " + this.getModel() + " model of " + this.getMake();
        return s;
    }
}
