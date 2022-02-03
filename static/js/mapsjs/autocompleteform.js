let address1Field
let autocomplete
function initAutocomplete() {
    address1Field = document.getElementById('addressAutocomplete');
    // Create the autocomplete object, restricting the search predictions to addresses in Kenya
    autocomplete = new google.maps.places.Autocomplete(address1Field, {
      componentRestrictions: { country: ["ke"] },
      fields: ["address_components", "geometry"],
    });
    address1Field.focus();
    autocomplete.addListener("place_changed", fillInAddress);
}
function fillInAddress() {
    // Get the place details from the autocomplete object.
    const place = autocomplete.getPlace();
    let address1 = "";
  
    // Get each component of the address from the place details,
    // and then fill-in the corresponding field on the form.
    // place.address_components are google.maps.GeocoderAddressComponent objects
    // which are documented at http://goo.gle/3l5i5Mr
    for (const component of place.address_components) {
        const componentType = component.types[0];
    
        switch (componentType) {
            case "street_number": {
            address1 = `${component.long_name} ${address1}`;
            break;
            }
    
            case "route": {
            address1 += component.short_name;
            break;
            }
    
            case "postal_code": {
            postcode = `${component.long_name}${postcode}`;
            break;
            }
    
            case "postal_code_suffix": {
            postcode = `${postcode}-${component.long_name}`;
            break;
            }
            case "locality":
            document.querySelector("#locality").value = component.long_name;
            break;
            case "administrative_area_level_1": {
            document.querySelector("#state").value = component.short_name;
            break;
            }
            case "country":
            document.querySelector("#country").value = component.long_name;
            break;
        }
    }
    
        address1Field.value = address1;
        postalField.value = postcode;
        // After filling the form with address components from the Autocomplete
        // prediction, set cursor focus on the second address line to encourage
        // entry of subpremise information such as apartment, unit, or floor number.
}

function transportFunction() {
    var form = document.getElementById("form");
    form.style.display = "block";
    var enquiry = document.getElementById("enquiry");
    enquiry.style.display = "none";
  }