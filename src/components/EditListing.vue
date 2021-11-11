<template>
  <form>
    <div
      class="
        shadow-xl
        border-2
        rounded
        px-8
        pt-6
        pb-8
        mb-4
        mt-6
        flex flex-col
        my-2
        m-auto
        w-3/4
      "
    >
      <h1
        class="
          block
          uppercase
          tracking-wide
          text-grey-darker text-xl
          font-bold
          mb-2
          mt-2
        "
      >
        Editing Listing #{{ id }}
      </h1>
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
              mt-6
            "
            >Position Title</label
          >
          <input
            class="
              outline-none
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              mb-6
            "
            required
            type="text"
            v-model="position"
          />
        </div>
        <div class="md:w-1/2 px-3">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
              mt-6
            "
            >Position Responsibilities</label
          >
          <textarea
            class="
              outline-none
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              mb-6
            "
            required
            type="text"
            v-model="pos_res"
          />
        </div>
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
              mt-6
            "
            >Minimum Qualifications</label
          >
          <textarea
            class="
              outline-none
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              mb-6
            "
            required
            type="text"
            v-model="min_qual"
          />
        </div>
      </div>
      <input required type="text" v-model="pref_qual" />
      <input required type="text" v-model="add_info" />
      <input required type="text" v-model="duration" />
      <input required type="text" v-model="app_open" />
      <input required type="text" v-model="app_close" />
    </div>
  </form>
</template>

<script>
export default {
  name: "EditListing",
  async mounted() {
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    let listing_id = params.get("id");
    let result = await fetch(
      `${process.env.SERVER_URL}/admin/get-listing/${listing_id}`
    ).catch((error) => {
      console.log(error);
    });
    let listing = await result.json();
    // TODO: NEEDS REFACTORING
    let l = listing.listing;
    this.id = l.id;
    this.position = l.position;
    this.pos_res = l.pos_responsibility;
    this.min_qual = l.min_qualifications;
    this.pref_qual = l.pref_qualifications;
    this.add_info = l.addition_info;
    this.duration = l.duration;
    this.app_open = l.app_open;
    this.app_close = l.app_close;
  },
  data() {
    return {
      id: 0,
      position: "",
      pos_res: "",
      min_qual: "",
      pref_qual: "",
      add_info: "",
      duration: "",
      app_open: "",
      app_close: "",
    };
  },
  methods: {
    updatePositionTitle() {
      console.log(this.position);
    },
  },
};
</script>
