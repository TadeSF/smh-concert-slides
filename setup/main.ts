import { defineAppSetup } from "@slidev/types";
import { library } from "@fortawesome/fontawesome-svg-core";
import VueVideoPlayer from "@videojs-player/vue";
import "video.js/dist/video-js.css";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faBell, faBellSlash } from "@fortawesome/free-solid-svg-icons";


export default defineAppSetup(({ app, router }) => {
  // Vue App
  library.add(faBell, faBellSlash);
  // Add fontawesome to vue app
  app.component("font-awesome-icon", FontAwesomeIcon);
  app.use(VueVideoPlayer);
});