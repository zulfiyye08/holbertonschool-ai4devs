1. Kod Keyfiyyəti və Refaktorinq (Code Quality & Refactoring)
Məqsəd: Mövcud kodu daha oxunaqlı, performanslı və sənaye standartlarına uyğun hala gətirmək.

Kodun Optimallaşdırılması:

Giriş: Mürəkkəb dövrlər (nested loops) və ya yüksək resurs tələb edən hesablamalar.

Çıxış: Zaman və yaddaş mürəkkəbliyi (Big O notation) optimallaşdırılmış səmərəli kod.

Dizayn Patternlərinin Tətbiqi:

Giriş: "Spaghetti" kod və ya təkrar olunan (redundant) funksionallıq.

Çıxış: Uyğun dizayn patterni (məsələn, Singleton, Strategy, Factory) tətbiq edilmiş struktur.

Legacy Kodun Müasirləşdirilməsi:

Giriş: Köhnəlmiş kitabxanalar və ya dəstəklənməyən sintaksis (məsələn, Python 2.x).

Çıxış: Müasir standartlara (məsələn, Python 3.12+, ES6+) uyğunlaşdırılmış kod.

2. Xətaların Tapılması və Sazlanması (Debugging & Error Handling)
Məqsəd: Koddakı məntiqi və texniki səhvləri aşkar edərək sistemi stabil hala gətirmək.

Stack Trace Analizi:

Giriş: Terminaldan alınan xəta mesajı və əlaqəli kod bloku.

Çıxış: Xətanın köklü səbəbinin (root cause) izahı və konkret həll kodu.

Təhlükəsizlik Boşluqlarının Təhlili:

Giriş: İstifadəçi girişləri, web formaları və ya verilənlər bazası sorğuları.

Çıxış: SQL Injection, XSS kimi boşluqların aradan qaldırıldığı, təmizlənmiş (sanitized) kod.

Məntiqi Səhvlərin (Logical Bugs) Təsbiti:

Giriş: İşləyən, lakin gözlənilən nəticəni verməyən funksiya.

Çıxış: Alqoritmdəki yanlışlığın izahı və düzəldilmiş məntiq.

3. Testləşdirmə (Testing)
Məqsəd: Proqramın müxtəlif şəraitlərdə düzgün işlədiyini avtomatlaşdırılmış testlərlə təsdiqləmək.

Unit Testlərin Yaradılması:

Giriş: Mövcud sinif (class) və ya funksiya.

Çıxış: Jest, PyTest və ya JUnit formatında yazılmış test ssenariləri.

Edge Case Ssenariləri:

Giriş: Məlumat qəbul edən API endpointləri.

Çıxış: Boş giriş, limit aşımı və ya yanlış tip kimi kənar hallar üçün test siyahısı.

Mock Məlumatların Hazırlanması:

Giriş: Verilənlər bazası sxemi (DB Schema).

Çıxış: Test mühiti üçün hazırlanmış JSON formatlı saxta (mock) datalar.

4. Sənədləşdirmə və Baxım (Documentation & Maintenance)
Məqsəd: Kodun digər tərtibatçılar tərəfindən asan başa düşülməsini və davamlılığını təmin etmək.

API Sənədlərinin Yaradılması:

Giriş: Sinif və metodların mənbə kodu.

Çıxış: Swagger, JSDoc və ya Markdown formatında peşəkar sənədlər.

Commit Mesajlarının Standartlaşdırılması:

Giriş: git diff çıxışı (dəyişikliklərin siyahısı).

Çıxış: Conventional Commits standartına (məsələn: feat:, fix:, refactor:) uyğun mesajlar.

Kod Şərhlərinin Əlavə Edilməsi:

Giriş: Sıx və mürəkkəb kod blokları.

Çıxış: Məntiqi izah edən daxili (inline) şərhlər və geniş Docstring-lər.
