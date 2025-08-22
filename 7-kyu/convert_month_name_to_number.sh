month="$1"
lower_month=$(echo "$month" | tr '[:upper:]' '[:lower:]')

case $lower_month in
    "jan" | "january")
        echo "01"
        ;;
    "feb" | "february")
        echo "02"
        ;;
    "mar" | "march")
        echo "03"
        ;;
    "apr" | "april")
        echo "04"
        ;;
    "may")
        echo "05"
        ;;
    "jun" | "june")
        echo "06"
        ;;
    "jul" | "july")
        echo "07"
        ;;
    "aug" | "august")
        echo "08"
        ;;
    "sep" | "september")
        echo "09"
        ;;
    "oct" | "october")
        echo "10"
        ;;
    "nov" | "november")
        echo "11"
        ;;
    "dec" | "december")
        echo "12"
        ;;
    *)
        echo "Invalid month: $month" >&2
        exit 1
        ;;
esac
