const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
 
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review_id");
        let reviewElement = document.getElementById(`review${reviewId}`);
 
        if (reviewElement) {
            let reviewContent = reviewElement.innerText;
            if (reviewText && reviewText.tagName === 'TEXTAREA') {
                reviewText.value = reviewContent;
            } else if (reviewText) {
                reviewText.innerText = reviewContent;
            }
 
            if (submitButton) {
                submitButton.innerText = "Update";
            }
 
            if (reviewForm) {
                reviewForm.setAttribute("action", `edit_review/${reviewId}`);
            }
        } else {
            console.error(`Review element with ID 'review${reviewId}' not found`);
        }
    });
}