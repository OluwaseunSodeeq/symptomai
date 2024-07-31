document.addEventListener('DOMContentLoaded', function() {
    // Initialize the chatbot, make user know their request is being processed 
    const sendbtn = document.getElementById('sendSymptom');
    const inputField = document.getElementById('symptomSearchBox');  
    const defaultContent = document.querySelector('.defaultContent');

    sendbtn.addEventListener('click', function(){
    inputField.value = "...";
    defaultContent.style.display = 'none';   
});


// Provide diagnostic response
   const symptomSearchBox = document.getElementById("symptomSearchBox");
   const sendSymptomButton = document.getElementById("sendSymptom");

   sendSymptomButton.addEventListener("click", function () {
     const symptoms = symptomSearchBox.value;
     if (symptoms.trim() === "") {
       alert("Please enter your symptoms.");
       return;
     }

     // Disable the input field and button
     symptomSearchBox.disabled = true;
     sendSymptomButton.style.pointerEvents = "none";

     fetch("https://symptomai-y0zm.onrender.com/diagnose", {
       method: "POST",
       headers: {
         "Content-Type": "application/json",
       },
       body: JSON.stringify({ symptoms: symptoms }),
     })
       .then((response) => response.json())
       .then((data) => {
         if (data.error) {
           alert(data.error);
           return;
         }
         const main = document.getElementById("main");
         const diagnosisDiv = document.createElement("div");
         diagnosisDiv.classList.add("diagnosis-result");
         diagnosisDiv.innerHTML = `
           <p>${data.diagnosis}</p>
           <img src="${data.confidence_score_image}" alt="Confidence Score" />
         `;
         main.appendChild(diagnosisDiv);
         symptomSearchBox.value = "";
       })
       .catch((error) => {
         console.error("Error:", error);
         alert("An error occurred while diagnosing. Please try again.");
       })
       .finally(() => {
         // Re-enable the input field and button
         symptomSearchBox.disabled = false;
         sendSymptomButton.style.pointerEvents = "auto";
       });
   });

});
