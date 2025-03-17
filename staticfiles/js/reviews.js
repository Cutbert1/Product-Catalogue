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


const deleteModalElement = document.getElementById("deleteModal");
 
    if (deleteModalElement) {
    const deleteModal = new bootstrap.Modal(deleteModalElement);
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
     
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-review_id");
            if (deleteConfirm) {
                deleteConfirm.href = `delete_review/${reviewId}`;
            }
            deleteModal.show();
        });
    }
} else {
    console.error("Issue with Modal");
}

