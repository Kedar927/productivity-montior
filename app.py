<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <title>
   Real-Time Productivity Monitoring with Face Login
  </title>
  <script src="https://cdn.tailwindcss.com">
  </script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&amp;display=swap" rel="stylesheet"/>
  <style>
   body {
      font-family: 'Inter', sans-serif;
    }
   #videoElement {
     border-radius: 0.5rem;
     background-color: #000;
     width: 100%;
     max-width: 480px;
     height: auto;
   }
   #login-section, #dashboard-section {
     max-width: 900px;
     margin-left: auto;
     margin-right: auto;
   }
   .hidden {
     display: none;
   }
  </style>
 </head>
 <body class="bg-gray-50 min-h-screen flex flex-col">
  <header class="bg-white shadow-md sticky top-0 z-50">
   <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
    <div class="flex items-center space-x-3">
     <img alt="Company logo, blue square with white letter P" class="h-10 w-10 rounded" height="40" src="https://storage.googleapis.com/a1aa/image/c8adad5a-5ff4-4ed8-7225-822f6b21dbc9.jpg" width="40"/>
     <h1 class="text-xl font-semibold text-gray-900">
      Productivity Monitor
     </h1>
    </div>
   </div>
  </header>

  <main class="flex-grow px-4 sm:px-6 lg:px-8 py-8 flex flex-col items-center">
   <!-- Login Section -->
   <section id="login-section" class="bg-white rounded-lg shadow p-6 w-full max-w-md flex flex-col items-center space-y-6">
    <h2 class="text-2xl font-semibold text-gray-900">
     Face Login
    </h2>
    <video autoplay muted playsinline id="videoElement" aria-label="Camera video feed for face login">
    </video>
    <button id="capture-face-btn" class="mt-4 w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500" type="button">
     <i class="fas fa-camera mr-2"></i> Capture Face &amp; Login
    </button>
    <p id="login-message" class="text-sm text-red-600 mt-2 min-h-[1.25rem]"></p>
   </section>

   <!-- Dashboard Section (hidden initially) -->
   <section id="dashboard-section" class="hidden w-full max-w-7xl flex flex-col space-y-12">
    <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">
     Real-Time Monitoring Dashboard
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
     <!-- Total Individuals Detected -->
     <div class="bg-white rounded-lg shadow p-6 flex items-center space-x-4">
      <div class="p-4 bg-blue-100 rounded-full text-blue-600">
       <i class="fas fa-users fa-2x">
       </i>
      </div>
      <div>
       <p class="text-sm font-medium text-gray-500">
        Individuals Detected
       </p>
       <p class="text-2xl font-bold text-gray-900" id="total-individuals">
        0
       </p>
      </div>
     </div>
     <!-- Productive Time Today -->
     <div class="bg-white rounded-lg shadow p-6 flex items-center space-x-4">
      <div class="p-4 bg-green-100 rounded-full text-green-600">
       <i class="fas fa-clock fa-2x">
       </i>
      </div>
      <div>
       <p class="text-sm font-medium text-gray-500">
        Total Productive Time (hrs)
       </p>
       <p class="text-2xl font-bold text-gray-900" id="productive-time">
        0.0
       </p>
      </div>
     </div>
     <!-- Break Time Today -->
     <div class="bg-white rounded-lg shadow p-6 flex items-center space-x-4">
      <div class="p-4 bg-yellow-100 rounded-full text-yellow-600">
       <i class="fas fa-coffee fa-2x">
       </i>
      </div>
      <div>
       <p class="text-sm font-medium text-gray-500">
        Total Break Time (hrs)
       </p>
       <p class="text-2xl font-bold text-gray-900" id="break-time">
        0.0
       </p>
      </div>
     </div>
    </div>
    <div class="mt-10 bg-white rounded-lg shadow p-6">
     <h3 class="text-xl font-semibold text-gray-900 mb-4">
      Zone Occupancy Overview
     </h3>
     <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="border border-gray-200 rounded-lg p-4">
       <h4 class="font-semibold text-blue-600 mb-2 flex items-center space-x-2">
        <i class="fas fa-desktop">
        </i>
        <span>
         Desks
        </span>
       </h4>
       <p class="text-4xl font-bold text-gray-900" id="desk-count">
        0
       </p>
       <p class="text-sm text-gray-500">
        Individuals currently at desks
       </p>
      </div>
      <div class="border border-gray-200 rounded-lg p-4">
       <h4 class="font-semibold text-green-600 mb-2 flex items-center space-x-2">
        <i class="fas fa-users">
        </i>
        <span>
         Meeting Rooms
        </span>
       </h4>
       <p class="text-4xl font-bold text-gray-900" id="meeting-count">
        0
       </p>
       <p class="text-sm text-gray-500">
        Individuals currently in meetings
       </p>
      </div>
      <div class="border border-gray-200 rounded-lg p-4">
       <h4 class="font-semibold text-yellow-600 mb-2 flex items-center space-x-2">
        <i class="fas fa-coffee">
        </i>
        <span>
         Break Areas
        </span>
       </h4>
       <p class="text-4xl font-bold text-gray-900" id="break-count">
        0
       </p>
       <p class="text-sm text-gray-500">
        Individuals currently on break
       </p>
      </div>
     </div>
    </div>
    <section id="reports" class="mb-12">
     <h2 class="text-3xl font-semibold text-gray-900 mb-6">
      Individual Time Reports &amp; Movement History
     </h2>
     <div class="overflow-x-auto bg-white rounded-lg shadow">
      <table class="min-w-full divide-y divide-gray-200">
       <thead class="bg-gray-50">
        <tr>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Person
         </th>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Desk Time (hrs)
         </th>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Meeting Time (hrs)
         </th>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Break Time (hrs)
         </th>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Current Zone
         </th>
         <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
          Movement History
         </th>
        </tr>
       </thead>
       <tbody class="bg-white divide-y divide-gray-200" id="individual-report">
       </tbody>
      </table>
     </div>
    </section>
   </section>
  </main>

  <footer class="bg-white border-t border-gray-200 py-6 text-center text-gray-500 text-sm">
   © 2024 Productivity Monitor. All rights reserved.
  </footer>

  <script>
   // Mobile menu toggle (not used here but kept for future)
   // Face Login & Movement Tracking Implementation

   const video = document.getElementById('videoElement');
   const captureBtn = document.getElementById('capture-face-btn');
   const loginMessage = document.getElementById('login-message');
   const loginSection = document.getElementById('login-section');
   const dashboardSection = document.getElementById('dashboard-section');
   const individualReportEl = document.getElementById('individual-report');

   // Simulated known faces database (face descriptors simulated by name)
   // In real app, this would be face embeddings or similar
   const knownFaces = [
     { id: 1, name: 'Alice Johnson' },
     { id: 2, name: 'Bob Smith' },
     { id: 3, name: 'Charlie Lee' },
     { id: 4, name: 'Diana Prince' },
     { id: 5, name: 'Ethan Hunt' },
     { id: 6, name: 'Fiona Gallagher' },
     { id: 7, name: 'George Martin' },
     { id: 8, name: 'Hannah Baker' },
     { id: 9, name: 'Ian Curtis' },
     { id: 10, name: 'Julia Roberts' },
     { id: 11, name: 'Kevin Durant' },
     { id: 12, name: 'Laura Palmer' },
     { id: 13, name: 'Michael Scott' },
     { id: 14, name: 'Nina Simone' },
     { id: 15, name: 'Oscar Wilde' },
   ];

   // Individuals data with time tracking and movement history
   const individuals = knownFaces.map((face) => ({
     id: face.id,
     name: face.name,
     currentZone: 'break', // default start zone
     deskTime: 0,
     meetingTime: 0,
     breakTime: 0,
     lastUpdate: Date.now(),
     movementHistory: [{ zone: 'break', timestamp: Date.now() }],
   }));

   // Settings
   let updateInterval = 5000; // milliseconds

   // Start webcam video stream
   async function startVideo() {
     try {
       const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: false });
       video.srcObject = stream;
     } catch (err) {
       loginMessage.textContent = 'Error accessing camera: ' + err.message;
     }
   }

   // Simulated face recognition function
   // In real app, this would use ML model to detect and recognize face from video frame
   // Here, we simulate by randomly picking a known face with 80% chance or fail
   function recognizeFace() {
     return new Promise((resolve) => {
       setTimeout(() => {
         if (Math.random() < 0.8) {
           // Pick random known face
           const face = knownFaces[Math.floor(Math.random() * knownFaces.length)];
           resolve(face);
         } else {
           resolve(null);
         }
       }, 1000); // simulate 1 second recognition delay
     });
   }

   // Login handler
   captureBtn.addEventListener('click', async () => {
     loginMessage.textContent = 'Recognizing face...';
     captureBtn.disabled = true;

     const recognizedFace = await recognizeFace();

     if (recognizedFace) {
       loginMessage.textContent = Welcome, ${recognizedFace.name}! Logging you in...;
       setTimeout(() => {
         loginSection.classList.add('hidden');
         dashboardSection.classList.remove('hidden');
         startMonitoring(recognizedFace.id);
       }, 1000);
     } else {
       loginMessage.textContent = 'Face not recognized. Please try again.';
     }
     captureBtn.disabled = false;
   });

   // Stop video stream on login to save resources
   function stopVideoStream() {
     if (video.srcObject) {
       video.srcObject.getTracks().forEach(track => track.stop());
       video.srcObject = null;
     }
   }

   // Update dashboard elements references
   const totalIndividualsEl = document.getElementById('total-individuals');
   const productiveTimeEl = document.getElementById('productive-time');
   const breakTimeEl = document.getElementById('break-time');
   const deskCountEl = document.getElementById('desk-count');
   const meetingCountEl = document.getElementById('meeting-count');
   const breakCountEl = document.getElementById('break-count');

   // Format number to 1 decimal place
   function formatHours(num) {
     return num.toFixed(1);
   }

   // Variables for monitoring
   let monitoringIntervalId = null;
   let loggedInUserId = null;

   // Simulate zone switching for all individuals except logged-in user (who we track precisely)
   function simulateMovementExceptUser(userId) {
     individuals.forEach((person) => {
       if (person.id !== userId) {
         if (Math.random() < 0.2) {
           const zones = ['desks', 'meeting', 'break'];
           let newZone;
           do {
             newZone = zones[Math.floor(Math.random() * zones.length)];
           } while (newZone === person.currentZone);
           person.currentZone = newZone;
           person.movementHistory.push({ zone: newZone, timestamp: Date.now() });
         }
       }
     });
   }

   // Simulate logged-in user movement by randomly changing zone every 15-30 seconds
   function simulateUserMovement(userId) {
     const user = individuals.find(p => p.id === userId);
     if (!user) return;
     const zones = ['desks', 'meeting', 'break'];
     let newZone;
     do {
       newZone = zones[Math.floor(Math.random() * zones.length)];
     } while (newZone === user.currentZone);
     user.currentZone = newZone;
     user.movementHistory.push({ zone: newZone, timestamp: Date.now() });
   }

   // Update dashboard counts and reports
   function updateDashboard() {
     const now = Date.now();

     let deskCount = 0;
     let meetingCount = 0;
     let breakCount = 0;

     let totalDeskTime = 0;
     let totalMeetingTime = 0;
     let totalBreakTime = 0;

     individuals.forEach((person) => {
       const elapsedHours = (now - person.lastUpdate) / (1000 * 60 * 60);
       if (person.currentZone === 'desks') {
         person.deskTime += elapsedHours;
         deskCount++;
       } else if (person.currentZone === 'meeting') {
         person.meetingTime += elapsedHours;
         meetingCount++;
       } else if (person.currentZone === 'break') {
         person.breakTime += elapsedHours;
         breakCount++;
       }
       person.lastUpdate = now;

       totalDeskTime += person.deskTime;
       totalMeetingTime += person.meetingTime;
       totalBreakTime += person.breakTime;
     });

     totalIndividualsEl.textContent = individuals.length;
     productiveTimeEl.textContent = formatHours(totalDeskTime);
     breakTimeEl.textContent = formatHours(totalBreakTime);

     deskCountEl.textContent = deskCount;
     meetingCountEl.textContent = meetingCount;
     breakCountEl.textContent = breakCount;

     // Update individual report table with movement history
     individualReportEl.innerHTML = '';
     individuals.forEach((person) => {
       const tr = document.createElement('tr');
       tr.className = 'hover:bg-gray-50';

       const zoneLabel = {
         desks: 'Desk',
         meeting: 'Meeting Room',
         break: 'Break Area',
       }[person.currentZone] || 'Unknown';

       // Format movement history as zone names with timestamps
       const movementStrings = person.movementHistory.map(mv => {
         const date = new Date(mv.timestamp);
         const timeStr = date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
         const zoneName = {
           desks: 'Desk',
           meeting: 'Meeting Room',
           break: 'Break Area',
         }[mv.zone] || 'Unknown';
         return ${zoneName} @ ${timeStr};
       }).join(' → ');

       tr.innerHTML = `
         <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">${person.name}</td>
         <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">${formatHours(person.deskTime)}</td>
         <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">${formatHours(person.meetingTime)}</td>
         <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">${formatHours(person.breakTime)}</td>
         <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">${zoneLabel}</td>
         <td class="px-6 py-4 whitespace-nowrap text-xs text-gray-600 max-w-xs truncate" title="${movementStrings}">${movementStrings}</td>
       `;
       individualReportEl.appendChild(tr);
     });
   }

   // Main monitoring loop
   function startMonitoring(userId) {
     loggedInUserId = userId;
     stopVideoStream();

     // Initial update
     updateDashboard();

     // Simulate user movement every 20 seconds
     setInterval(() => {
       simulateUserMovement(loggedInUserId);
     }, 20000);

     // Simulate others movement every update interval
     monitoringIntervalId = setInterval(() => {
       simulateMovementExceptUser(loggedInUserId);
       updateDashboard();
     }, updateInterval);
   }

   // Start video on page load
   startVideo();
  </script>
 </body>
</html>
<script src="https://127.0.0.1:5000/"
""