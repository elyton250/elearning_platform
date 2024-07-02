
document.addEventListener("DOMContentLoaded", function() {
    const enrollButtons = document.querySelectorAll(".enroll-button");
    enrollButtons.forEach(button => {
        button.addEventListener("click", toggleConfirmation);
    });

    function toggleConfirmation(event) {
        const row = event.target.closest("tr");
        const confirmationSpan = row.querySelector(".confirmation");
        const enrollButton = row.querySelector(".enroll-button");
        confirmationSpan.style.display = "inline-block";

        const confirmButton = confirmationSpan.querySelector(".confirm-button");
        const cancelButton = confirmationSpan.querySelector(".cancel-button");

        // confirmButton.addEventListener("click", () => {
        //     row.remove();
        //     // Perform additional delete logic here (e.g., update database)
        // });

        cancelButton.addEventListener("click", () => {
            confirmationSpan.style.display = "none";
            deleteButton.style.display = "block";
        });

        enrollButton.style.display = "none";
    }
});
