function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('app_ciudadano');
}

function doPost(e) {
  var action = e.parameter.action;
  
  switch(action) {
    case 'registrarAlerta':
      return registrarAlerta(e.parameter);
    case 'getDNIsSerenos':
      return getDNIsSerenos();
    case 'getEstadoSereno':
      return getEstadoSereno(e.parameter.dni);
    case 'getNumerosParte':
      return getNumerosParte(e.parameter.dni);
    case 'getInfoIncidente':
      return getInfoIncidente(e.parameter.numeroParte);
    case 'actualizarEstado':
      return actualizarEstado(e.parameter);
    default:
      return ContentService.createTextOutput('Acción no reconocida');
  }
}

function registrarAlerta(datos) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Ciudadanos');
  var lastRow = sheet.getLastRow();
  var numeroParte = 'PO-' + (lastRow + 1).toString().padStart(7, '0');
  var fechaHora = new Date().toLocaleString('es-PE');
  
  sheet.appendRow([
    fechaHora,
    numeroParte,
    datos.nombres,
    datos.apellidos,
    datos.dni,
    datos.celular,
    datos.tipo,
    datos.subtipo,
    datos.modalidad,
    datos.latitud,
    datos.longitud,
    'Alerta'
  ]);
  
  return ContentService.createTextOutput('Alerta registrada con éxito');
}

function getDNIsSerenos() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Serenos');
  var dnis = sheet.getRange(2, 1, sheet.getLastRow() - 1, 1).getValues();
  return ContentService.createTextOutput(JSON.stringify(dnis.flat())).setMimeType(ContentService.MimeType.JSON);
}

function getEstadoSereno(dni) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Serenos');
  var dniColumn = sheet.getRange('A:A').getValues();
  var row = dniColumn.findIndex(function(r) { return r[0] == dni }) + 1;
  var estado = sheet.getRange(row, 13).getValue(); // Asumiendo que el estado está en la columna 13
  return ContentService.createTextOutput(estado);
}

function getNumerosParte(dni) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Ciudadanos');
  var numeros = sheet.getRange('B2:B').getValues().flat().filter(String);
  return ContentService.createTextOutput(JSON.stringify(numeros)).setMimeType(ContentService.MimeType.JSON);
}

function getInfoIncidente(numeroParte) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Ciudadanos');
  var numeroParteColumn = sheet.getRange('B:B').getValues();
  var row = numeroParteColumn.findIndex(function(r) { return r[0] == numeroParte }) + 1;
  var info = sheet.getRange(row, 1, 1, sheet.getLastColumn()).getValues()[0];
  return ContentService.createTextOutput(JSON.stringify(info)).setMimeType(ContentService.MimeType.JSON);
}

function actualizarEstado(datos) {
  var sheetCiudadanos = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Ciudadanos');
  var sheetSerenos = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Serenos');
  
  // Actualizar estado en la hoja Ciudadanos
  var numeroParteColumn = sheetCiudadanos.getRange('B:B').getValues();
  var rowCiudadano = numeroParteColumn.findIndex(function(r) { return r[0] == datos.numeroParte }) + 1;
  sheetCiudadanos.getRange(rowCiudadano, 12).setValue(datos.nuevoEstado); // Asumiendo que el estado está en la columna 12
  
  // Actualizar estado en la hoja Serenos
  var dniColumn = sheetSerenos.getRange('A:A').getValues();
  var rowSereno = dniColumn.findIndex(function(r) { return r[0] == datos.dni }) + 1;
  sheetSerenos.getRange(rowSereno, 13).setValue(datos.nuevoEstado); // Asumiendo que el estado está en la columna 13
  
  return ContentService.createTextOutput('Estado actualizado con éxito');
}