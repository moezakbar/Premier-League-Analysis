/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This class creates an object that represents the owner of the vehicle
 * it creates instance variables that are specific to the ownner of the vehicle
 */
public class CarOwner {
    // declare instance variables
    private String name;
    private int age;
    private int licenseNumber;
    private int yearsDriving;

    /**
     * This is the constructor of the class
     * @param name a sting
     * @param age an int
     * @param licenseNumber an int
     * @param yearsDriving an int
     * @throws IllegalVehicle an exception class
     */
    public CarOwner(String name, int age, int licenseNumber, int yearsDriving) throws IllegalVehicle {

        // call the setters to set values of instance variables
        setName(name);
        setAge(age);
        setLicenseNumber(licenseNumber);
        setYearsDriving(yearsDriving);
    }

    // setters

    /**
     * This is the setter for name
     * @param name a string
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * This is the setter for age and it also checks for illegal values
     * @param age an int
     * @throws IllegalVehicle an exception class
     */
    public void setAge(int age) throws IllegalVehicle {

        // check if the age is an illegal value
        if (age < 0) {
            // throw an exception
            throw new IllegalVehicle("Illegal value!");
        }

        this.age = age;
    }

    /**
     * This is the setter for licenseNumber
     * @param licenseNumber an int
     */
    public void setLicenseNumber(int licenseNumber) {
        this.licenseNumber = licenseNumber;
    }

    /**
     * This is the setter for yearsDriving and also checks for illegal values
     * @param yearsDriving an int
     * @throws IllegalVehicle an exception class
     */
    public void setYearsDriving(int yearsDriving) throws IllegalVehicle {

        // check if the value is an illegal value
        if (yearsDriving < 0) {
            // throw an exception
            throw new IllegalVehicle("Illegal value!");
        }

        this.yearsDriving = yearsDriving;
    }

    // getters

    /**
     * This is a getter for name
     * @return name
     */
    public String getName() {
        return this.name;
    }

    /**
     * This is a getter for age
     * @return age
     */
    public int getAge() {
        return this.age;
    }

    /**
     * This is a getter for licenseNumber
     * @return licenseNumber
     */
    public int getLicenseNumber() {
        return this.licenseNumber;
    }

    /**
     * This is a getter for yearsDriving
     * @return yearsDriving
     */
    public int getYearsDriving() {
        return this.yearsDriving;
    }

    /**
     * This function overrides the toString method of the parent class
     * @return s
     */
    public String toString(){
        String s = "The name of the car owner is " + this.getName() + " and is " + this.getAge() +
        " years old. Owner's license number is " + getLicenseNumber() + " and has been driving for " +
        this.getYearsDriving() + " years.";
        return s;
    }
}
