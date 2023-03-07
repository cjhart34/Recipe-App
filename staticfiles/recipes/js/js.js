function search_recipe() {
    let input = document.getElementById('searchbar').value
    input = input.toLowerCase();
    let recipes = document.getElementsByClassName('recipe_searched');

    let recipe_box = document.getElementsByClassName('search_results');
    recipe_box[0].style.display = "block";

    for (i = 0; i < recipes.length; i++) {
        if (!recipes[i].innerHTML.toLowerCase().includes(input)) {
            recipes[i].style.display = "none";
        }
        else {
            recipes[i].style.display = "block";
        }
    }
    if (input == "") {
        recipe_box[0].style.display = "none";
    }
}