let costs = {
    "hp": [5000, 35000],
    "nokia": [7000, 25000],
    "samsung": [35000, 80000],
    "motorola": [12000, 40000],
    "apple": [50000, 120000]
};

$("button").click(() => {
    event.preventDefault();

    const index = $("mobile-or-desktop").is(":checked") ? 0 : 1;
    const brand = $("#brands").val();
    const quantity = parseInt($("#quantity").val());

    const cost = costs[brand][index] * quantity;

    alert(`The cost of ${brand} is ${cost}.`);
});
