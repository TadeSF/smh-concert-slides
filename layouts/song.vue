<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-center items-center h-52 overflow-hidden p-8">
      <img class="max-h-full max-w-full" src="../img/logo_inv.svg" alt="Logo" />
    </div>
    <div class="flex-1 flex justify-between m-10 gap-4">
      <div class="flex-1 flex flex-col justify-center items-center text-center">
        <h1>{{ composer }}</h1>
        <h3 v-if="supertitle">{{ supertitle }}</h3>
        <h2>{{ name }}</h2>
        <h3 v-if="subtitle">{{ subtitle }}</h3>
      </div>
      <div class="flex-1 flex flex-col justify-center items-center relative">
        <div
          v-for="(line, index) in updatedLyrics"
          :key="index"
          :class="['wheel', getWheelClass(index)]"
        >
          <p>{{ line }}</p>
        </div>
      </div>
    </div>
    <span
      v-for="(line, index) in shortenedMovementListForClickCount"
      :key="index"
    >
      <span v-click></span>
  </span>
  </div>
</template>

<script>
export default {
  props: {
    composer: { type: String, default: "" },
    name: { type: String, default: "" },
    supertitle: { type: String, default: "" },
    subtitle: { type: String, default: "" },
    lyrics: { type: Array, default: () => [] },
  },
  computed: {
    currentStep() {
      // The '+' converts the string to a number.
      return +this.$route.query.clicks || 0;
    },
    shortenedMovementListForClickCount() {
      // Shortens the list by 1 for the current click count.
      return this.lyrics.slice(0, -1);
    },
    updatedLyrics() {
      let updatedLyrics = [];

      updatedLyrics.push("");
      updatedLyrics.push("");

      for (let i = 0; i < this.lyrics.length; i++) {
        updatedLyrics.push(this.lyrics[i]);
      }

      updatedLyrics.push("");
      updatedLyrics.push("");

      return updatedLyrics;
    },
  },
  methods: {
    getWheelClass(index) {
      const wheelPosition = index - this.currentStep;

      if (wheelPosition === 0) {
        return "wheel--first";
      } else if (wheelPosition === 1) {
        return "wheel--second";
      } else if (wheelPosition === 2) {
        return "wheel--third";
      } else if (wheelPosition === 3) {
        return "wheel--fourth";
      } else if (wheelPosition === 4) {
        return "wheel--fifth";
      } else if (wheelPosition < 0) {
        return "wheel--hidden--before";
      } else {
        return "wheel--hidden--after";
      }
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  /* Uppercase */
  text-transform: uppercase;
  color: #e5013b;
}

h2 {
  font-size: 2em;
  font-weight: bold;
}

h3 {
  font-size: 1.5em;
  font-weight: normal;
  margin-top: 0;
}

.wheel {
  transition: all 1.5s ease-out;
  transition: opacity 0.5 ease-out;
  opacity: 0%;
  color: #fff;
  position: absolute;
  text-align: center;
  width: 100%;
  font-size: 1.2rem;
}

.wheel p {
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.wheel--hidden--before {
  transform: translate(0, -4.5em);
  opacity: 0%;
}
.wheel--first {
  transform: translate(0, -3.5em);
  opacity: 20%;
}

.wheel--second {
  transform: translate(0, -2em);
  opacity: 50%;
}

.wheel--third {
  transform: translate(0, 0);
  opacity: 100%;
}

.wheel--fourth {
  transform: translate(0, 2em);
  opacity: 50%;
}

.wheel--fifth {
  transform: translate(0, 3.5em);
  opacity: 20%;
}

.wheel--hidden--after {
  transform: translate(0, 4.5em);
  opacity: 0%;
}
</style>
