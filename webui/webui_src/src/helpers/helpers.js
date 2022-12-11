import {DateTime} from "@/helpers/luxon";

const locale = localStorage.getItem('userLocal') || 'en'
const formateTime = (datetime) => {
  return DateTime.fromISO(datetime).toLocaleString()
}
const timeAgo = (date) => {
  return DateTime.fromISO(date).setLocale(locale).toRelative()
}
const upperCaser = (text) => {
  return text.toUpperCase();
}

export default {
  formateTime, timeAgo, upperCaser
}
