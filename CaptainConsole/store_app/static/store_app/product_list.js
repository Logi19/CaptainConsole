"use strict";

// Get current GET parameters from URL and fill in filter checkboxes if currently applied
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

/**
 * Change 'order=' GET parameter in URL and reload site.
 * @param {String} new_order New GET parameter for ordering
 */
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

/**
 * Change 'page=' GET parameter and reload site (pagination).
 * @param {String} new_page Page number (pagination)
 */
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
