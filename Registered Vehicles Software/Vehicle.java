/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This class is the parent class for all vehicles.
 * It creates instance variables that are shared by all child classes.
 * It also creates setters and getters for these instance variables to be accessed/modified.
 */
public class Vehicle {
    // declare instance variables
    private int registrationNumber;
    private CarOwner owner;
    private int odometerReading;
    private String make;
    private String model;
    private int year;
    private int numWheels;
    private String plateNumber;

    /**
     * Constructor for Vehicle class
     * @param registrationNumber an int
     * @param owner an object representing owner of vehicle
     * @param odometerReading an int representing mileage of vehicle
     * @param make a string
     * @param model a string
     * @param year an int representing model year
     * @param numWheels an int
     * @param plateNumber a string
     * @throws IllegalVehicle an exception class that handles illegal values
     */
    public Vehicle(int registrationNumber,CarOwner owner,int odometerReading,String make,String model,int year,
            int numWheels,String plateNumber) throws IllegalVehicle {
        // call all the getters to set values of the instance variables
        setRegistrationNumber(registrationNumber);
        setOwner(owner);
        setMake(make);
        setModel(model);
        setOdometerReading(odometerReading);
        setYear(year);
        setNumWheels(numWheels);
        setPlateNumber(plateNumber);
    }

    // setters

    /**
     * setter registrationNumber
     * @param registrationNumber an int
     */
    public void setRegistrationNumber(int registrationNumber){
        this.registrationNumber = registrationNumber;
    }

    /**
     * setter for Owner
     * @param owner an object
     */
    public void setOwner(CarOwner owner){
        this.owner = owner;
    }

    /**
     * setter for Make
     * @param make a string
     */
    public void setMake(String make){
        this.make = make;
    }

    /**
     * a setter for Model
     * @param model a string
     */
    public void setModel(String model){
        this.model = model;
    }

    /**
     * setter for odometerReading and also checks for illegal values
     * @param odometerReading an int
     * @throws IllegalVehicle an exception class
     */
    public void setOdometerReading(int odometerReading) throws IllegalVehicle {

        // check if the new odometerReading is same as old one
        if (odometerReading <= this.odometerReading){

            // throw an exception
            throw new IllegalVehicle("Illegal mileage - nice try!");
        }

        this.odometerReading = odometerReading;
    }

    /**
     * setter for year and checks for illegal values
     * @param year an int
     * @throws IllegalVehicle an exception class
     */
    public void setYear(int year) throws IllegalVehicle {
        // check for illegal values
        if (year < 1980){

            throw new IllegalVehicle("Illegal year - you need to buy a newer vehicle!");
        }

        this.year = year;
    }

    /**
     * setter for numWheels and checks for illegal values
     * @param numWheels an int
     * @throws IllegalVehicle an exception class
     */
    public void setNumWheels(int numWheels) throws IllegalVehicle {
        // check for illegal values
        if (numWheels < 2) {

            throw new IllegalVehicle("Illegal number of wheels - buy a unicycle!");
        }

        this.numWheels = numWheels;
    }

    /**
     * setter for plateNumber
     * @param plateNumber a string
     * @throws IllegalVehicle an exception class
     */
    public void setPlateNumber(String plateNumber) throws IllegalVehicle {

        // call the fucntion that checks if the plateNumber is legal
        boolean value = checkPlateNumber(plateNumber);

        // if value is false
        if (!value) {

            throw new IllegalVehicle("Illegal license plate!");
        }

        this.plateNumber = plateNumber;
    }

    // getters

    /**
     * getter for registrationNumber
     * @return registrationNumber
     */
    public int getRegistrationNumber(){
        return this.registrationNumber;
    }

    /**
     * getter for owner
     * @return owner
     */
    public CarOwner getOwner(){
        return this.owner;
    }

    /**
     * getter for Make
     * @return Make
     */
    public String getMake(){
        return this.make;
    }

    /**
     * getter for model
     * @return model
     */
    public  String getModel(){
        return this.model;
    }

    /**
     * getter for odometerReading
     * @return odometerReading
     */
    public int getOdometerReading(){
        return this.odometerReading;
    }

    /**
     * getter for year
     * @return year
     */
    public int getYear(){
        return this.year;
    }

    /**
     * getter for numWheels
     * @return numWheels
     */
    public int getNumWheels(){
        return this.numWheels;
    }

    /**
     * getter for plateNumber
     * @return plateNumber
     */
    public String getPlateNumber(){
        return this.plateNumber;
    }

    /**
     * This function checks if the plateNumber contains legal values
     * @param plateNumber an int
     * @return True if legal
     *         False if illegal
     */
    private boolean checkPlateNumber(String plateNumber){

        // declare counters
        int digit = 0;
        int alphabet = 0;

        if (plateNumber.length() == 7) {
            for (int i = 0; i < 4; i++) {

                // check to see if the character in iteration is an alphabet
                if (Character.isLetter(plateNumber.charAt(i))) {
                    // add 1 to the counter for alphabets
                    alphabet += 1;
                }
            }

            for (int i = 4; i < plateNumber.length(); i++) {

                // check to see if the character in iteration is a digit
                if (Character.isDigit(plateNumber.charAt(i))) {
                    // add 1 to the counter for digits
                    digit += 1;
                }
            }

            // check to see if number of alphabets and digits are legal values
            if ((alphabet == 4) && (digit == 3)) {
                return true;
            } else {
                return false;
            }

        } else {
            return false;
        }


    }

    /**
     * This function prints detais about the object
     * @return s a string
     */
    public String toString(){
        String s = "This Vehicle is the " + this.year + " " + this.model + " model of " + this.make;
        return s;
    }

}
