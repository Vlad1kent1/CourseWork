export const updateApplication = (id, applicationData) => {
  console.log(applicationData);
  return fetch(`https://coursework.test.azuremicroservices.io/spring-app-20240522080612/default/applications/update/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(applicationData),
  })
    .then(() => {
      console.log("Application Updated");
    })
    .catch((error) => console.error("Error updating application:", error));
};
