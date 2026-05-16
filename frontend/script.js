async function predictStress() {
    const data = {
        sleep_hours: document.getElementById("sleep").value,
        heart_rate: document.getElementById("heart").value,
        study_hours: document.getElementById("study").value,
        screen_time: document.getElementById("screen").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        "Stress Level: " + result.stress_level;
}