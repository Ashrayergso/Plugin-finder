```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('search-button').addEventListener('click', searchPlugin);
    document.getElementById('version-check').addEventListener('click', checkVersion);
});

function searchPlugin() {
    let pluginName = document.getElementById('plugin-name').value;
    fetch(`/plugin_scanner/search_plugin?name=${pluginName}`)
        .then(response => response.json())
        .then(data => {
            if (data.plugin_found) {
                populatePluginTable(data.plugin_data);
            } else {
                alert('Plugin not found');
            }
        });
}

function checkVersion() {
    let pluginName = document.getElementById('plugin-name').value;
    fetch(`/plugin_scanner/check_version?name=${pluginName}`)
        .then(response => response.json())
        .then(data => {
            if (data.version_checked) {
                alert(`The most recent version of ${pluginName} is ${data.latest_version}`);
            } else {
                alert('Could not check version');
            }
        });
}

function populatePluginTable(pluginData) {
    let table = document.getElementById('plugin-table');
    table.innerHTML = '';
    pluginData.forEach(plugin => {
        let row = table.insertRow();
        row.insertCell().innerHTML = plugin.name;
        row.insertCell().innerHTML = plugin.version;
        row.insertCell().innerHTML = plugin.creator;
        row.insertCell().innerHTML = plugin.installation_date;
    });
}
```