export const addApplication = (applicationData) => {
  console.log(applicationData);
  return fetch("https://coursework.test.azuremicroservices.io/spring-app-20240522080612/default/applications/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(applicationData),
  })
    .then(() => {
      console.log("New Application Added");
    })
    .catch((error) => {
      console.error("Error adding new application:", error);
    });
};
