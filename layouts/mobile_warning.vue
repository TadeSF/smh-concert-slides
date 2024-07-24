<template>
  <div class="flex flex-col h-full justify-center items-center">
    <div class="flex flex-col justify-center items-center gap-20">
      <div class="flex-1 flex justify-center items-center gap-8">
        <p :class="parantheseClass">(</p>
        <p :class="parantheseClass">(</p>
        <p :class="parantheseClass">(</p>
        <font-awesome-icon :icon="['fas', 'bell']" :class="iconClassBell" />
        <font-awesome-icon
          :icon="['fas', 'bell-slash']"
          :class="iconClassBellSlash"
        />
        <p :class="parantheseClass">)</p>
        <p :class="parantheseClass">)</p>
        <p :class="parantheseClass">)</p>
      </div>
      <div class="flex-1 flex flex-col justify-center items-center gap-4">
        <transition name="fade">
        <h1 v-if="showText" class="text-4xl font-bold ">{{ title }}</h1>
        </transition>
        <transition name="fade">
        <h2 v-if="showText" class="text-3xl font-bold">{{ subtitle }}</h2>
        </transition>
      </div>
    </div>
    <slot />
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

export default {
  data() {
    return {
      iconClassBell: 'fa-shake icon transition-all duration-1000 opacity-100', // Initial icon class
      iconClassBellSlash: 'icon-slash transition-all duration-1000 opacity-0',
      parantheseClass: 'icon-wave opacity-100',
      title: "Bitte schalten Sie Ihre Mobiltelefone aus",
      subtitle: "Please turn off your mobile devices",
      showText: true,
    };
  },
  methods: {
    updateText() {
      this.showText = false;

      setTimeout(() => {
        this.title = "Vielen Dank!";
        this.subtitle = "Thank you!";
        this.showText = true;
      }, 500);
    }
  },
  mounted() {
    setTimeout(() => {
      this.iconClassBell = 'icon transition-all duration-1000 opacity-0'; // Add transition class
      this.iconClassBellSlash = 'icon-slash transition-all duration-1000 opacity-100'; // Remove transition class
      this.parantheseClass = 'icon-wave opacity-0';
    }, 5600);
    setTimeout(() => {
      this.updateText();
    }, 9000);
  }
};
</script>

<style scoped>
.icon {
  font-size: 10em;
  color: #e5013b;
}

.icon-slash {
  font-size: 10em;
  color: #ffffff;
  position: absolute; /* Add position absolute */
}

h1 {
  color: #ffffff;
}

h2 {
  color: #e5013b;
}

@keyframes wave {
  25% {
    scale: 1;
    opacity: 0;
  }
  50% {
    scale: 1.2;
    opacity: 100;
  }
  75% {
    scale: 1;
    opacity: 0;
  }
}

.icon-wave {
  color: #e5013b;
  opacity: 0;
  font-size: 5em;
  transition: all 2s ease-out;
  animation-name: wave;
  animation-duration: 1.8s;
  animation-iteration-count: 3;
}

.icon-wave:nth-child(2),
.icon-wave:nth-child(7) {
  animation-delay: 0.3s;
  font-size: 8em;
}

.icon-wave:nth-child(1),
.icon-wave:nth-child(8) {
  animation-delay: 0.6s;
  font-size: 11em;
}

.duration-500 {
  transition-duration: 500ms;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
