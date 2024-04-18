package org.example.carparking.controller;

import javafx.event.ActionEvent;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import org.example.carparking.CarParkingDAO;
import org.example.carparking.data.CarParking;

public class AddCarParkingController {

    private CarParkingDAO carParkingDAO = new CarParkingDAO();
    public TextField brandModelInput;
    public TextField licensePlateInput;
    public TextField ownerPhoneInput;
    public TextField parkingHourInput;
    public TextField prepaidHourInput;
    private Stage stage;
    private MainController mainController;
    public void setStage(Stage newWindow) {
        stage = newWindow;
    }

    public void setMainController(MainController mainController) {
        this.mainController = mainController;
    }

    public void onSubmitButtonPress(ActionEvent actionEvent) {
        String brandModel = brandModelInput.getText();
        String licensePlate = licensePlateInput.getText();
        String ownerPhone = ownerPhoneInput.getText();
        int parkingHour = Integer.parseInt(parkingHourInput.getText());
        int prepaidHours = Integer.parseInt(prepaidHourInput.getText());

        CarParking record = new CarParking(brandModel, licensePlate, ownerPhone, parkingHour, prepaidHours);
        carParkingDAO.createCar(record);
        mainController.refresh();

        stage.close();
    }
}
