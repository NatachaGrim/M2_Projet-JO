// Création de la couche de tuiles
var tiles = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png', {
    maxZoom: 8, // Niveau de zoom maximum réduit
    minZoom: 2, // Niveau de zoom minimum réduit
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> Service numérique de la recherche / INHA'
});

// Définition de la position initiale de la carte
var latlng = L.latLng(48.1351253, 11.5819806);

// Création de la carte
var map = L.map('map', {
    center: latlng,
    zoom: 4, // Zoom initial réduit
    layers: [tiles]
});

// Création des clusters de marqueurs pour chaque année
var a_1996 = L.markerClusterGroup({
    disableClusteringAtZoom: 2 // Désactiver le regroupement des marqueurs lorsque le zoom est inférieur à 2
});
var a_2000 = L.markerClusterGroup({
    disableClusteringAtZoom: 2
});
var a_2004 = L.markerClusterGroup({
    disableClusteringAtZoom: 2
});
var a_2008 = L.markerClusterGroup({
    disableClusteringAtZoom: 2
});
var a_2012 = L.markerClusterGroup({
    disableClusteringAtZoom: 2
});
var a_2016 = L.markerClusterGroup({
    disableClusteringAtZoom: 2
});


// Création des marqueurs pour chaque année et ajout aux clusters correspondants
L.geoJson(geojson_RAMA, {
    pointToLayer: function(feature, latlng) {
        var medailles = feature.properties["M\u00e9dailles"];
        var annee = feature.properties.Annees;
        var color;
        var legend;
        // Déterminer la couleur et la légende en fonction du nombre de médailles
        if (medailles < 10) {
            color = 'saddlebrown';
            legend = 'Moins de 10 médailles';
        } else if (medailles < 30) {
            color = 'silver';
            legend = 'Entre 10 et 30 médailles';
        } else {
            color = 'gold';
            legend = 'Plus de 30 médailles';
        }
        // Créer le cercle avec la couleur définie
        var circle = L.circleMarker(latlng, {
            color: color,
            radius: 10,
            fillOpacity: 0.7 // Opacité du remplissage réduite
        });

        // Créer le contenu de la popup avec les données spécifiques à chaque année
        var popupContent =
            "<h3 style='text-align: center'>" + feature.properties.Pays + "</h3>" +
            "<table>" +
            "<tr><td><i class='fas fa-calendar-day'></i> Année: </td><td>" + annee + "</td></tr>" +
            "<tr><td><i class='fas fa-medal'></i> Médailles: </td><td>" + medailles + "</td></tr>" +
            "<tr><td><i class='fas fa-users'></i> Population: </td><td>" + feature.properties.Population + "</td></tr>" +
            "<tr><td><i class='fas fa-money-bill-wave'></i> Richesse: </td><td>" + feature.properties.Richesse + "</td></tr>" +
            "<tr><td><i class='fas fa-chart-line'></i> Investissement: </td><td>" + feature.properties.Investissements + "</td></tr>" +
            "</table>";

        // Ajouter la popup au marqueur
        circle.bindPopup(popupContent);

        // Ajouter le marqueur au cluster correspondant selon l'année
        switch (annee) {
            case 1996:
                a_1996.addLayer(circle);
                break;
            case 2000:
                a_2000.addLayer(circle);
                break;
            case 2004:
                a_2004.addLayer(circle);
                break;
            case 2008:
                a_2008.addLayer(circle);
                break;
            case 2012:
                a_2012.addLayer(circle);
                break;
            case 2016:
                a_2016.addLayer(circle);
                break;
        }

        // Retourner le marqueur
        return circle;
    }
});


// Ajout d'un titre à la carte en manipulant le DOM
var mapTitle = L.control({ position: "topright" });

mapTitle.onAdd = function(map) {
    var div = L.DomUtil.create("div", "map-title");
    div.innerHTML = "<h2>Carte interactive des résultats aux Jeux Olympiques (1996-2016)</h2>";
    return div;
};

mapTitle.addTo(map);
// Création d'un panneau de contrôle pour les clusters
var overlayMaps = {
    "1996": a_1996,
    "2000": a_2000,
    "2004": a_2004,
    "2008": a_2008,
    "2012": a_2012,
    "2016": a_2016
};
L.control.layers(null, overlayMaps, { collapsed: false }).addTo(map);

// Ajout de la légende
var legend = L.control({ position: 'bottomright' });
legend.onAdd = function(map) {
    var div = L.DomUtil.create('div', 'info legend');
    div.innerHTML +=
        '<h4 class="legend-title">Légende</h4>' +
        '<div><i class="legend-circle" style="background: saddlebrown;"></i> Moins de 10 médailles</div>' +
        '<div><i class="legend-circle" style="background: silver;"></i> Entre 10 et 30 médailles</div>' +
        '<div><i class="legend-circle" style="background: gold;"></i> Plus de 30 médailles</div>';
    return div;
};
legend.addTo(map);

