package org.example.carparking;

import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Root;
import org.example.carparking.data.CarParking;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.util.List;

public class CarParkingDAO {

    private static SessionFactory sessionFactory = HibernateUtil.getSessionFactory();

    public static CarParking get(long id) {
        Session session = sessionFactory.openSession();
        CarParking obj = session.get(CarParking.class, id);
        session.close();
        return obj;
    }

    public static void createCar(CarParking obj) {
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();
        session.persist(obj);
        tx.commit();
        session.close();
    }

    public static List<CarParking> getAll() {
        try (Session session = sessionFactory.openSession()) {
            CriteriaBuilder builder = session.getCriteriaBuilder();
            CriteriaQuery<CarParking> query = builder.createQuery(CarParking.class);
            Root<CarParking> root = query.from(CarParking.class);
            query.select(root);
            return session.createQuery(query).getResultList();
        }
    }

    public static void updateCar(CarParking obj) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();
            session.merge(obj);
            tx.commit();
        }
    }

    public static void deleteCar(CarParking obj) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();
            session.delete(obj);
            tx.commit();
        }
    }
}
