export const deleteApplication = (id) => {
    return fetch(`https://coursework.test.azuremicroservices.io/spring-app-20240522080612/default/applications/delete/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text().then(text => {
            return text ? JSON.parse(text) : {};
        });
    })
    .catch(error => {
        console.error('There was a problem with the delete operation:', error);
    });
};
