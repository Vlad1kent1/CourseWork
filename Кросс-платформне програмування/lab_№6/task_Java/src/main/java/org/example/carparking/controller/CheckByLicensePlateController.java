package org.example.carparking.controller;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import org.example.carparking.CarParkingDAO;
import org.example.carparking.data.CarParking;

import java.util.ArrayList;
import java.util.List;

public class CheckByLicensePlateController {
    public TextField licensePlateInput;
    public TextField currentHourInput;

    public ListView licensePlateList;
    private Stage stage;
    private MainController mainController;

    public void setStage(Stage newWindow) {
        stage = newWindow;
    }

    public void setMainController(MainController mainController) {
        this.mainController = mainController;
    }

    public void onCheckButtonPress(ActionEvent actionEvent) {
        String license_plate = licensePlateInput.getText();
        int hour = Integer.parseInt(currentHourInput.getText());
        List<String> carParkingInfoList = new ArrayList<>();
        List<CarParking> carParkingList = CarParkingDAO.getAll();
        for (CarParking carParking : carParkingList) {
            if (license_plate.equals(carParking.getLicense_plate()) && Math.abs(hour - carParking.getParking_hour()) < carParking.getPrepaid_hours()) {
                String carParkingInfo = carParking.toString() + "\nYes";
                carParkingInfoList.add(carParkingInfo);
            }
        }
        licensePlateList.setItems(FXCollections.observableArrayList(carParkingInfoList));
    }
}
