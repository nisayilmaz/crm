<template>
  <div class="nav-wrapper position-relative end-0">
    <ul class="nav nav-pills nav-fill p-1" role="tablist">
      <li class="nav-item">
        <a
          class="nav-link mb-0 px-0 py-1 active active"
          role="tab"
          aria-selected="true"
          >Tüm Notlar</a
        >
      </li>
      <li class="nav-item">
        <a
          class="nav-link mb-0 px-0 py-1"
          role="tab"
          aria-selected="false"
          >Arama</a
        >
      </li>
      <li class="nav-item">
        <a
          class="nav-link mb-0 px-0 py-1"
          role="tab"
          aria-selected="false"
          >Yüzyüze Görüşme</a
        >
      </li>
      <li class="nav-item">
        <a
          class="nav-link mb-0 px-0 py-1"
          role="tab"
          aria-selected="false"
          >İş Ortağı İle Görüşme</a
        >
      </li>
        <li class="nav-item">
            <a
                  class="nav-link mb-0 px-0 py-1"
                  role="tab"
                  aria-selected="false"
            >E-posta</a
            >
        </li>
    </ul>
  </div>
</template>

<script>
import setNavPills from "@/assets/js/nav-pills.js";

export default {
  name: "NavPill",
  mounted() {
    setNavPills();
  },
};
</script>
