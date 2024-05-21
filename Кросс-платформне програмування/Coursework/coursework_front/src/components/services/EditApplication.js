export const updateApplication = (id, applicationData) => {
  console.log(applicationData);
  return fetch(`http://localhost:8080/applications/update/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(applicationData),
  })
    .then(() => {
      console.log("Application Updated");
    })
    .catch((error) => console.error("Error updating application:", error));
};
