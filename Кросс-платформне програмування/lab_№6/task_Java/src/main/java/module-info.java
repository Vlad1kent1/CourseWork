module org.example.carparking {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
    requires jakarta.persistence;
    requires org.hibernate.orm.core;
    requires java.naming;

    opens org.example.carparking to javafx.fxml;
    opens org.example.carparking.data;
    exports org.example.carparking;
    exports org.example.carparking.controller;
    opens org.example.carparking.controller to javafx.fxml;
}