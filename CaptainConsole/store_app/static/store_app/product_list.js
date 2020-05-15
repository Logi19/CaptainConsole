const params = new URLSearchParams(window.location.search);
const manuf_params = params.getAll("manufacturer");
const platform_params = params.getAll("platform");
const type_params = params.getAll("type");

manuf_params.forEach((item_id) => {
    document.getElementById(item_id.replace(/ /g, "+")).setAttribute("checked", "checked");
});

platform_params.forEach((item_id) => {
    document.getElementById(item_id.replace(/ /g, "+")).setAttribute("checked", "checked");
});

type_params.forEach((item_id) => {
    document.getElementById(item_id.replace(/ /g, "+")).setAttribute("checked", "checked");
});

function change_order(new_order) {
    if (new_url.indexOf("order=") > -1) {
        new_url = new_url.replace(/order=(year|name|price)-(asc|desc)/, new_order);
    } else {
        if (new_url.endsWith("products/")) {
            new_url += "?" + new_order;
        } else {
            new_url += "&" + new_order;
        }
    }
    window.location = new_url;
}

function change_page(new_page) {
    if (curr_url.indexOf("page=") > -1) {
        curr_url = curr_url.replace(/page=[0-9]/, new_page);
    } else {
        if (curr_url.endsWith("products/")) {
            curr_url += "?" + new_page;
        } else {
            curr_url += "&" + new_page;
        }
    }
    window.location = curr_url;
}
