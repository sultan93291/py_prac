def http_status(status):
  match status :
    case  200 :
      return("ok")
    case 404:
      return("Not Found")
    case 400:
      return("Bad Request")
    case 500:
      return("Internal Server Error")
    case _:
      return("unknown status code")


print(http_status(500))