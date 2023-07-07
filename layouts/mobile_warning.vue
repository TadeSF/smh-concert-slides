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
        <h1 class="text-4xl font-bold">
          Bitte schalten Sie Ihr Mobiltelefon aus
        </h1>
        <h2 class="text-3xl font-bold">Please turn off your mobile devices</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      iconClassBell: 'fa-shake icon transition-all duration-1000 opacity-100', // Initial icon class
      iconClassBellSlash: 'icon-slash transition-all duration-1000 opacity-0',
      parantheseClass: 'icon-wave opacity-100'
    };
  },
  mounted() {
    setTimeout(() => {
      this.iconClassBell = 'icon transition-all duration-1000 opacity-0'; // Add transition class
      this.iconClassBellSlash = 'icon-slash transition-all duration-1000 opacity-100'; // Remove transition class
      this.parantheseClass = 'icon-wave opacity-0';
    }, 5600);
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
</style>
