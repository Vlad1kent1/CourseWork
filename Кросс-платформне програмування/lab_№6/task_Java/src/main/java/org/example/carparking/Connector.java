package org.example.carparking;

import java.lang.reflect.InvocationTargetException;
import java.sql.*;

public class Connector {
    private String dataBaseUrl;
    private String dataBaseUser;
    private String dataBasePassword;
    private String driverClass;
    public Connector(String dataBaseName) {
        this.dataBaseUrl = "jdbc:mysql://localhost:3306/carparking?useSSL=false&serverTimezone=UTC";
        this.dataBaseUser = "root";
        this.dataBasePassword = "Jazon0507&";
        this.driverClass = "com.mysql.cj.jdbc.Driver";
    }
    public boolean testDriver(){
        try{
            Class.forName(driverClass)
                    .getDeclaredConstructor().newInstance();
            return true;
        }catch (ClassNotFoundException e) {
            e.printStackTrace();
            return false;
        } catch (IllegalAccessException e) {
            e.printStackTrace();
            return false;
        } catch (InstantiationException e) {
            e.printStackTrace();
            return false;
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
            return false;
        } catch (InvocationTargetException e) {
            e.printStackTrace();
            return false;
        }
    }
    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(dataBaseUrl,
                dataBaseUser,dataBasePassword);
    }
}
