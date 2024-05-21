// validations.js
import dayjs from 'dayjs';

export const validateDestination = (destination) => {
  const destinationPattern = /^[A-Z][a-zA-Z ]*$/;
  return destinationPattern.test(destination);
};

export const validateFlightNumber = (flightNumber) => {
  const flightNumberPattern = /^[A-Z]{2} \d{3,4}$/;
  return flightNumberPattern.test(flightNumber);
};

export const validatePassengerName = (name) => {
  const namePattern = /^[A-Z][a-z]+ [A-Z]\.[A-Z]\.$/;
  return namePattern.test(name);
};

export const validateDate = (date) => {
  if( !date ) return false;
  return date.isAfter(dayjs());
};
