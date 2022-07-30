/*
Name: Abdul Moez Akbar
Date: 29th July'2022
 */
package Assignment2;

/**
 * This is a class that extends the Exception class.
 * It prints a custom message whenever an IllegalVehicle exception is thrown
 */
public class IllegalVehicle extends Exception {

    /**
     * This is the constructor for this class
     * @param message a String that represents the message that will be printed
     */
    public IllegalVehicle(String message) {

        // calls the print message function of the parent(Exception) class
        super(message);

    } // end exception
}
