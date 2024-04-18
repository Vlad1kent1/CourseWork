module org.example.task_java {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.task_java to javafx.fxml;
    exports org.example.task_java;
}