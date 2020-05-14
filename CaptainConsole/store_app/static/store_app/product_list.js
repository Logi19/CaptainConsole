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
