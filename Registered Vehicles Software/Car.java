/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This class is a sub-class of Vehicle class.
 * It shares all the instances of its parent class and creates two new ones as well
 */
public class Car extends Vehicle{

    // declare instance variables
    private int numSeats;
    private boolean isSUV;  // True if car is an SUV

    /**
     * This is the constructor for the class
     * @param registrationNumber an int
     * @param owner an object
     * @param odometerReading an int
     * @param make a string
     * @param model a string
     * @param year an int
     * @param numWheels an int
     * @param plateNumber a string
     * @param numSeats an int
     * @param isSUV boolean
     * @throws IllegalVehicle an exception class
     */
    public Car(int registrationNumber,CarOwner owner,int odometerReading,String make,String model,int year,
               int numWheels,String plateNumber,int numSeats,boolean isSUV) throws IllegalVehicle {

        // call the contructor of the parent class
        super(registrationNumber,owner,odometerReading,make,model,year,numWheels,plateNumber);
        // call the setters to set value
        setNumSeats(numSeats);
        setIsSUV(isSUV);
    }

    // setters

    /**
     * This is a setter for numSeats
     * @param numSeats int
     */
    public void setNumSeats(int numSeats){
        this.numSeats = numSeats;
    }

    /**
     * This is a setter for isSUV
     * @param isSUV boolean
     */
    public  void setIsSUV(boolean isSUV){
        this.isSUV = isSUV;
    }

    //getters

    /**
     * This is a getter for numSeats
     * @return numSeats
     */
    public int getNumSeats(){
        return this.numSeats;
    }

    /**
     * This is a getter for isSUV
     * @return isSUV
     */
    public boolean getIsSUV(){
        return this.isSUV;
    }

    /**
     * This function overrides the parent class's toString method
     * @return s a string
     */
    public String toString() {
        String s = "";
        s += "This car is the " + this.getYear() + " " + this.getModel() + " model of " + this.getMake()
                + ". It contains " + this.getNumSeats() + " number of seats.";

        // check if car is an SUV
        if (this.isSUV == true) {
            s += "It is also an SUV.";
        }
        return s;
    }


}
