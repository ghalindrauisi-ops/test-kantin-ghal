/* ==============================================================================
   FILE: static/js/main.js
   PROYEK: Kantin Fasilkom UI - Website Development (DDP1)
   DESKRIPSI: Script interaktif untuk Sidebar Hamburger, Denah Pemetaan Interaktif,
              dan Logika Pengacakan (Randomizer).
   ============================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Inisialisasi seluruh modul fitur
  initSidebar();
  initFloorplanMap();
  initRandomizer();
});

/* ==============================================================================
   1. MODUL SIDEBAR NAVIGATION & HAMBURGER
   ============================================================================== */
function initSidebar() {
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const closeSidebarBtn = document.getElementById('closeSidebarBtn');
  const sidebarOverlay = document.getElementById('sidebarOverlay');

  if (!hamburgerBtn || !sidebarOverlay) return;

  // Fungsi membuka sidebar
  function openSidebar() {
    sidebarOverlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Kunci scroll halaman saat sidebar aktif
  }

  // Fungsi menutup sidebar
  function closeSidebar() {
    sidebarOverlay.classList.remove('active');
    document.body.style.overflow = ''; // Kembalikan scroll halaman
  }

  // Event Listener Klik
  hamburgerBtn.addEventListener('click', openSidebar);

  if (closeSidebarBtn) {
    closeSidebarBtn.addEventListener('click', closeSidebar);
  }

  // Tutup sidebar saat klik di area gelap (backdrop overlay) di luar menu
  sidebarOverlay.addEventListener('click', (event) => {
    if (event.target === sidebarOverlay) {
      closeSidebar();
    }
  });

  // Tutup sidebar jika user menekan tombol Escape (ESC) pada keyboard
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && sidebarOverlay.classList.contains('active')) {
      closeSidebar();
    }
  });
}

/* ==============================================================================
   2. MODUL MAPPING KANTIN INTERAKTIF
   ============================================================================== */
function initFloorplanMap() {
  const boothNodes = document.querySelectorAll('.booth-node');
  const infoPanel = document.getElementById('boothInfoPanel');

  if (!boothNodes.length || !infoPanel) return;

  boothNodes.forEach(node => {
    node.addEventListener('click', () => {
      // Hapus kelas 'active' dari semua node
      boothNodes.forEach(n => n.classList.remove('active'));
      
      // Tambahkan status 'active' ke node yang baru diklik
      node.classList.add('active');

      // Ambil metadata booth dari attribute dataset HTML
      const id = node.dataset.id;
      const name = node.dataset.name;
      const location = node.dataset.location;
      const description = node.dataset.description;
      const totalMenu = node.dataset.totalMenu;
      const detailUrl = node.dataset.detailUrl;

      // Update isi panel informasi booth di samping peta
      infoPanel.innerHTML = `
        <div style="animation: fadeIn 0.3s ease-out;">
          <span class="result-badge" style="background:#dbeafe; color:#1e40af;">Booth Terpilih</span>
          <h3 style="font-size:1.5rem; font-weight:800; color:var(--primary-dark); margin:0.5rem 0;">${name}</h3>
          <p style="font-size:0.875rem; color:var(--primary-light); font-weight:600; margin-bottom:1rem;">📍 ${location}</p>
          
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:1rem; margin-bottom:1.25rem;">
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.5;">${description}</p>
          </div>

          <p style="font-size:0.9rem; font-weight:700; margin-bottom:1.5rem;">
            🍽️ Total Menu: <span style="color:var(--primary);">${totalMenu} Pilihan Menu</span>
          </p>

          <a href="${detailUrl}" class="btn btn-primary btn-block">
            Buka Menu Booth Ini →
          </a>
        </div>
      `;
    });
  });
}

/* ==============================================================================
   3. MODUL RANDOMIZER MAKANAN, MINUMAN & KOMBO
   Mode baru: 'makanan', 'minuman', 'combo' (menggantikan booth/all_menu/specific_booth)
   ============================================================================== */
function initRandomizer() {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const modeInput = document.getElementById('randomizerModeInput');
  const facultyFilterGroup = document.getElementById('facultyFilterGroup');
  const budgetFilterGroup = document.getElementById('budgetFilterGroup');
  const randomizerForm = document.getElementById('randomizerForm');
  const resultContainer = document.getElementById('randomizerResultContainer');
  const randomizeBtn = document.getElementById('randomizeBtn');

  if (!tabButtons.length || !randomizerForm) return;

  // -----------------------------------------------------------------------
  // Pergantian Tab: Makanan / Minuman / Combo
  // Setiap tab mengubah nilai hidden input 'mode' dan menyesuaikan UI filter
  // -----------------------------------------------------------------------
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Hapus status aktif dari semua tab, lalu pasang ke tab yang diklik
      tabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const selectedMode = btn.dataset.mode;
      modeInput.value = selectedMode;

      // Mode 'combo': sembunyikan filter budget karena harga tampil sebagai total
      // Mode 'makanan' atau 'minuman': tampilkan filter budget dan filter fakultas
      if (selectedMode === 'combo') {
        if (budgetFilterGroup) budgetFilterGroup.style.display = 'none';
        if (facultyFilterGroup) facultyFilterGroup.style.display = 'block';
      } else {
        // makanan atau minuman
        if (budgetFilterGroup) budgetFilterGroup.style.display = 'block';
        if (facultyFilterGroup) facultyFilterGroup.style.display = 'block';
      }
    });
  });

  // -----------------------------------------------------------------------
  // Submit Form via AJAX (Fetch API) — tanpa reload halaman
  // -----------------------------------------------------------------------
  randomizerForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const mode = modeInput.value;
    const facultySelect = document.getElementById('facultySelect');
    const maxPriceInput = document.getElementById('maxPriceInput');

    const facultyId = facultySelect ? facultySelect.value : '';
    // Budget hanya relevan untuk mode makanan & minuman, bukan combo
    const maxPrice = (mode !== 'combo' && maxPriceInput) ? maxPriceInput.value : '';

    // Efek tombol loading saat proses berlangsung
    const originalBtnText = randomizeBtn.innerHTML;
    randomizeBtn.disabled = true;
    randomizeBtn.innerHTML = '🎲 Mengacak Pilihan...';

    // Bangun URL ke backend Django dengan parameter GET
    const url = `/randomizer/?mode=${encodeURIComponent(mode)}&faculty_id=${encodeURIComponent(facultyId)}&max_price=${encodeURIComponent(maxPrice)}&format=json`;

    fetch(url, {
      headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.message || 'Gagal mengacak data'); });
      }
      return response.json();
    })
    .then(data => {
      if (data.status === 'success' && data.data) {
        renderRandomizerResult(data.data);
      }
    })
    .catch(error => {
      alert(error.message || 'Terjadi kendala saat menghubungkan ke database.');
    })
    .finally(() => {
      randomizeBtn.disabled = false;
      randomizeBtn.innerHTML = originalBtnText;
    });
  });

  // -----------------------------------------------------------------------
  // Render Hasil ke Layar berdasarkan item.type
  // Mendukung: 'menu' (makanan/minuman tunggal), 'combo' (paket 2 kartu)
  // -----------------------------------------------------------------------
  function renderRandomizerResult(item) {
    if (!resultContainer) return;

    if (item.type === 'combo') {
      // ---- RENDER PAKET KOMBO: dua kartu berdampingan ----
      const food = item.food;
      const drink = item.drink;
      resultContainer.innerHTML = `
        <div class="result-box">
          <div style="text-align:center; margin-bottom:1.25rem;">
            <span class="result-badge" style="background:linear-gradient(135deg,#f59e0b,#ef4444);color:white;font-size:1rem;padding:0.4rem 1.2rem;">
              🍱 Paket Kombo Terpilih!
            </span>
            <p style="margin-top:0.75rem;color:var(--text-muted);font-size:0.9rem;">
              Satu makanan + satu minuman, langsung siap santap!
            </p>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:1.5rem;">
            <!-- Kartu Makanan -->
            <div style="background:#fff7ed;border:2px solid #fed7aa;border-radius:var(--radius-md);padding:1.25rem;">
              <div style="font-size:1.75rem;margin-bottom:0.5rem;">🍛</div>
              <span style="background:#f97316;color:white;font-size:0.72rem;font-weight:800;padding:0.2rem 0.6rem;border-radius:999px;">MAKANAN</span>
              <h4 style="font-size:1.1rem;font-weight:800;color:var(--primary-dark);margin:0.6rem 0 0.4rem;">${food.name}</h4>
              <p style="font-size:1rem;font-weight:800;color:#f97316;margin-bottom:0.5rem;">${food.formatted_price}</p>
              <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.3rem;">🏪 ${food.booth_name}</p>
              <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">🏛️ ${food.faculty_short} · ${food.canteen_name}</p>
              <p style="font-size:0.82rem;color:var(--text-secondary);line-height:1.5;">${food.description}</p>
              <a href="/booth/${food.booth_id}/" class="btn btn-secondary btn-block" style="margin-top:0.75rem;font-size:0.82rem;">Lihat Booth →</a>
            </div>

            <!-- Kartu Minuman -->
            <div style="background:#eff6ff;border:2px solid #bfdbfe;border-radius:var(--radius-md);padding:1.25rem;">
              <div style="font-size:1.75rem;margin-bottom:0.5rem;">🥤</div>
              <span style="background:#3b82f6;color:white;font-size:0.72rem;font-weight:800;padding:0.2rem 0.6rem;border-radius:999px;">MINUMAN</span>
              <h4 style="font-size:1.1rem;font-weight:800;color:var(--primary-dark);margin:0.6rem 0 0.4rem;">${drink.name}</h4>
              <p style="font-size:1rem;font-weight:800;color:#3b82f6;margin-bottom:0.5rem;">${drink.formatted_price}</p>
              <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.3rem;">🏪 ${drink.booth_name}</p>
              <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.75rem;">🏛️ ${drink.faculty_short} · ${drink.canteen_name}</p>
              <p style="font-size:0.82rem;color:var(--text-secondary);line-height:1.5;">${drink.description}</p>
              <a href="/booth/${drink.booth_id}/" class="btn btn-secondary btn-block" style="margin-top:0.75rem;font-size:0.82rem;">Lihat Booth →</a>
            </div>
          </div>

          <!-- Total Harga Kombo -->
          <div style="background:linear-gradient(135deg,#fef3c7,#fde68a);border:2px solid #fbbf24;border-radius:var(--radius-md);padding:1.1rem 1.5rem;text-align:center;margin-bottom:1rem;">
            <p style="font-size:0.85rem;color:#92400e;font-weight:600;margin-bottom:0.25rem;">💰 Total Harga Paket Kombo</p>
            <p style="font-size:1.75rem;font-weight:900;color:#b45309;">${item.formatted_total_price}</p>
            <p style="font-size:0.78rem;color:#92400e;margin-top:0.25rem;">
              ${food.formatted_price} + ${drink.formatted_price}
            </p>
          </div>

          <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;">
            <button type="button" class="btn btn-accent" onclick="document.getElementById('randomizeBtn').click();">
              🎲 Acak Kombo Lagi!
            </button>
          </div>
        </div>
      `;

    } else if (item.type === 'menu') {
      // ---- RENDER MENU TUNGGAL (Makanan atau Minuman) ----
      resultContainer.innerHTML = `
        <div class="result-box">
          <div style="display:flex;gap:0.5rem;align-items:center;margin-bottom:0.75rem;flex-wrap:wrap;">
            <span class="result-badge">🎉 Menu Terpilih</span>
            <span class="team-pill team-pill-accent" style="font-size:0.7rem;">Makan Apa Hari Ini?</span>
          </div>
          <h3 class="result-title">${item.name}</h3>
          <div class="result-meta">
            <span class="result-price">${item.formatted_price}</span>
            <span style="background:#e0f2fe;color:#0369a1;padding:0.25rem 0.75rem;border-radius:999px;font-size:0.85rem;font-weight:800;">
              🏛️ ${item.faculty_short} (${item.canteen_name})
            </span>
            <span class="result-booth">🏪 Stan: <strong>${item.booth_name}</strong></span>
            <span style="background:#f1f5f9;color:var(--text-muted);padding:0.25rem 0.65rem;border-radius:999px;font-size:0.8rem;font-weight:700;">
              ${item.category}
            </span>
          </div>
          <p class="result-desc">${item.description}</p>
          <div style="display:flex;gap:1rem;flex-wrap:wrap;">
            <a href="/booth/${item.booth_id}/" class="btn btn-primary">Kunjungi Booth ${item.booth_name} →</a>
            <button type="button" class="btn btn-secondary" onclick="document.getElementById('randomizeBtn').click();">🎲 Acak Ulang</button>
          </div>
        </div>
      `;
    }

    // Scroll halus ke area hasil
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}
