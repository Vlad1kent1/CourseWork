module org.example.carparking {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.carparking to javafx.fxml;
    exports org.example.carparking;
}