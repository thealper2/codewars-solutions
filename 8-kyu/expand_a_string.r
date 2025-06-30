expand <- function(s){
  if (nchar(s) == 0) {
    return(character(0))
  }
  strsplit(s, "")[[1]]
}