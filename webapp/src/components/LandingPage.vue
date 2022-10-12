<template>
    <div class="main-container d-flex">
        <div class="title-container d-flex flex-column">
          <span class="main-title">Welcome to Just 4 Work</span>
          <span class="slogan-title">Solutions for you workspace in one site</span>
        </div>
        <div class="cards-container">
            <b-card
                title="Shift timer"
                :img-src="shift_tracker_image"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2">
                <b-card-text>
                  Easily start your shift timer and have access to all the logs.
                </b-card-text>
                <b-button variant="primary">+ Info</b-button>
            </b-card>
            <b-card
                title="Task management"
                :img-src="task_app_image"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2">
                <b-card-text>
                  Keep track of your teams task effectively.
                </b-card-text>
                <b-button variant="primary">+ Info</b-button>
            </b-card>
            <b-card
                title="Employee registery"
                :img-src="employee_info_image"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2">
                <b-card-text>
                  Manage all the information of your team.
                </b-card-text>
                <b-button variant="primary">+ Info</b-button>
            </b-card>
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
        shift_tracker_image: "https://images.unsplash.com/photo-1431499012454-31a9601150c9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8dGltZXJ8ZW58MHx8MHx8&w=1000&q=80",
        task_app_image: "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dG9kb3xlbnwwfHwwfHw%3D&w=1000&q=80",
        employee_info_image:"https://media.istockphoto.com/photos/running-over-the-terms-and-conditions-in-her-contract-picture-id888776672?b=1&k=20&m=888776672&s=170667a&w=0&h=zHThH21Ht8tlxtysPy-sYpfR6-xtJq1S6Y1e1u5-R-Q="
      }
    },
    methods: {
    }
}
</script>

<style scoped>

.main-container {
  width: 100vw;
  height: 90vh;
  background: #212121;
  background-image: url("../assets/images/landing-page/bg-img.jpeg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover ;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}
.title-container {
  color: #f2f2f2;
  font-family: monospace, Georgia, 'Times New Roman', Times, serif;
}
.main-title {
  font-size: 70px;
  font-weight: bold;
}
.cards-container {
  display: flex;
  column-gap: 30px;
}
</style>