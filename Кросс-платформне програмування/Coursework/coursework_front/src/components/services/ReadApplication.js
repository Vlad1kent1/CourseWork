export const fetchApplications = (setApplication) => {
    return fetch("https://coursework.test.azuremicroservices.io/spring-app-20240522080612/default/applications/read")
      .then((res) => res.json())
      .then((result) => {
        setApplication(result);
        console.log(result);
      })
      .catch((error) => {
        console.error("Error fetching applications:", error);
      });
  };