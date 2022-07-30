/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This class is a subclass of Vehicle class
 * it shares all the instance variables of the parent class and creates two of its own
 */
public class Truck extends Vehicle{

    // declare instance variables
    private boolean isSemi;  // True if it is a transport truck
    private int loadCapacity; // weight truck can hold

    /**
     * This is the constructor for the class
     * @param registrationNumber an int
     * @param owner an object
     * @param odometerReading an int
     * @param make a string
     * @param model a string
     * @param year an int
     * @param numWheels an int
     * @param plateNumber an int
     * @param isSemi boolean
     * @param loadCapacity an int
     * @throws IllegalVehicle an exception class
     */
    public Truck(int registrationNumber, CarOwner owner, int odometerReading, String make, String model,
                 int year, int numWheels, String plateNumber, boolean isSemi, int loadCapacity) throws IllegalVehicle {

        // call the constructor of the parent class
        super(registrationNumber, owner, odometerReading, make, model, year, numWheels, plateNumber);
        // call setters to set value
        setIsSemi(isSemi);
        setLoadCapacity(loadCapacity);
    }

    // getters

    /**
     * This is a getter for loadCapacity
     * @return loadCapacity
     */
    public int getLoadCapacity() {
        return this.loadCapacity;
    }

    /**
     * This is a getter for isSemi
     * @return isSemi
     */
    public boolean getIsSemi() {
        return this.isSemi;
    }

    // setters

    /**
     * This is a setter for loadCapacity
     * @param loadCapacity an int
     */
    public void setLoadCapacity(int loadCapacity) {
        this.loadCapacity = loadCapacity;
    }

    /**
     * This is a setter for isSemi
     * @param isSemi a boolean
     */
    public void setIsSemi(boolean isSemi) {
        this.isSemi = isSemi;
    }

    /**
     * This function gets the number of axles in the truck by dividing its number of wheels by 2
     * @return axles an int
     */
    public float getNumberAxles() {

        // call the getter for number of wheels in the truck
        int wheels = this.getNumWheels();
        // divide the number of wheels by 2 and assign it to a variable
        float axles = wheels / 2;
        return axles;
    }

    /**
     * This function overrides the toString method of the parent class
     * @return s
     */
    public String toString() {
        String s = "";
        s += "This Truck is the " + this.getYear() + " " + this.getModel() + " model of " + this.getMake()
                + ". This truck has " + this.getNumberAxles() + " number of axles" + " and it can hold " +
                this.loadCapacity + " pounds.";

        // check if the transport truck variable is set to true
        if (this.isSemi == true) {
            s += " It is also a transport truck.";
        }
        return s;
    }
}
