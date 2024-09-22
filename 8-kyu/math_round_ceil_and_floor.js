function roundIt(n){
  let splitted_number = n.toString().split(".");
  if ((splitted_number[0].length) > (splitted_number[1].length)) {
    return Math.floor(n);    
  } else if ((splitted_number[0].length) < (splitted_number[1].length)) {
    return Math.ceil(n);
  } else {
    return Math.round(n);
  }
}