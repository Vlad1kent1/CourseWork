export const addApplication = (applicationData) => {
  console.log(applicationData);
  return fetch("http://localhost:8080/applications/add", {
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
