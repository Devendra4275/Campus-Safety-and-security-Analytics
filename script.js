const form = document.getElementById("incidentForm");
const incidentList = document.getElementById("incidentList");

form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = {
        type: formData.get("type"),
        location: formData.get("location"),
        time: formData.get("time"),
        description: formData.get("description")
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/report_incident", {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });

        if (res.ok) {
            alert("Incident reported successfully!");
            form.reset();
            loadIncidents();
        } else {
            alert("Failed to report incident.");
        }
    } catch (error) {
        console.error("Error submitting form:", error);
        alert("Error: Could not connect to backend.");
    }
});

async function loadIncidents() {
    try {
        const res = await fetch("http://127.0.0.1:8000/get_incidents");
        const incidents = await res.json();

        if (incidents.length === 0) {
            incidentList.innerHTML = "<p>No incidents reported yet.</p>";
            return;
        }

        incidentList.innerHTML = incidents.map(incident => `
            <div class="incident">
                <strong>${incident.type}</strong> at <strong>${incident.location}</strong><br>
                <em>${new Date(incident.time).toLocaleString()}</em><br>
                ${incident.description}
                <hr>
            </div>
        `).join("");
    } catch (error) {
        console.error("Error fetching incidents:", error);
        incidentList.innerHTML = "<p>Error loading incidents.</p>";
    }
}

// Load incidents on page load and refresh every 5 seconds
loadIncidents();
setInterval(loadIncidents, 5000);
