"""Test suite for package sorter."""

from package_sorter import sort


class TestStandardPackages:
    """Test STANDARD classification."""

    def test_small_light_package(self) -> None:
        assert sort(10, 10, 10, 5) == "STANDARD"

    def test_boundary_below_bulky_volume(self) -> None:
        assert sort(99, 99, 99, 10) == "STANDARD"

    def test_boundary_below_heavy_mass(self) -> None:
        assert sort(50, 50, 50, 19.9) == "STANDARD"


class TestBulkyPackages:
    """Test packages classified as bulky."""

    def test_bulky_by_volume_exact(self) -> None:
        assert sort(100, 100, 100, 10) == "SPECIAL"

    def test_bulky_by_volume_over(self) -> None:
        assert sort(200, 200, 200, 5) == "SPECIAL"

    def test_bulky_by_width(self) -> None:
        assert sort(150, 10, 10, 5) == "SPECIAL"

    def test_bulky_by_height(self) -> None:
        assert sort(10, 150, 10, 5) == "SPECIAL"

    def test_bulky_by_length(self) -> None:
        assert sort(10, 10, 150, 5) == "SPECIAL"

    def test_bulky_by_dimension_over(self) -> None:
        assert sort(200, 10, 10, 5) == "SPECIAL"


class TestHeavyPackages:
    """Test packages classified as heavy."""

    def test_heavy_exact_boundary(self) -> None:
        assert sort(10, 10, 10, 20) == "SPECIAL"

    def test_heavy_over_boundary(self) -> None:
        assert sort(50, 50, 50, 25) == "SPECIAL"


class TestRejectedPackages:
    """Test REJECTED classification."""

    def test_heavy_and_bulky_by_volume(self) -> None:
        assert sort(100, 100, 100, 20) == "REJECTED"

    def test_heavy_and_bulky_by_dimension(self) -> None:
        assert sort(150, 10, 10, 20) == "REJECTED"

    def test_very_heavy_and_very_bulky(self) -> None:
        assert sort(200, 200, 200, 50) == "REJECTED"


class TestEdgeCases:
    """Test edge cases and boundaries."""

    def test_volume_boundary_minus_one(self) -> None:
        assert sort(99.9, 100, 100, 10) == "STANDARD"

    def test_dimension_boundary_minus_one(self) -> None:
        assert sort(149, 10, 10, 10) == "STANDARD"

    def test_mass_boundary_minus_epsilon(self) -> None:
        assert sort(50, 50, 50, 19.99999) == "STANDARD"

    def test_all_boundaries_just_under(self) -> None:
        assert sort(149, 50, 50, 19.9) == "STANDARD"

    def test_minimal_dimensions(self) -> None:
        assert sort(1, 1, 1, 0.1) == "STANDARD"

    def test_zero_mass(self) -> None:
        assert sort(10, 10, 10, 0) == "STANDARD"

    def test_exact_volume_boundary_with_floats(self) -> None:
        assert sort(100.0, 100.0, 100.0, 10) == "SPECIAL"

    def test_just_under_volume_with_precision(self) -> None:
        assert sort(99.99999, 100, 100, 10) == "STANDARD"

    def test_multiple_paths_to_rejected(self) -> None:
        assert sort(150, 150, 150, 20) == "REJECTED"

    def test_bulky_by_dimension_and_volume(self) -> None:
        assert sort(200, 200, 200, 10) == "SPECIAL"

    def test_very_small_positive_values(self) -> None:
        assert sort(0.1, 0.1, 0.1, 0.01) == "STANDARD"

    def test_large_dimensions_under_both_boundaries(self) -> None:
        assert sort(149, 50, 50, 19.9) == "STANDARD"

    def test_high_dimensions_bulky_by_volume(self) -> None:
        assert sort(149.9, 149.9, 149.9, 19.9) == "SPECIAL"

    def test_one_zero_dimension(self) -> None:
        assert sort(0, 100, 100, 10) == "STANDARD"

    def test_mixed_int_float_inputs(self) -> None:
        assert sort(100, 100.0, 100, 20.0) == "REJECTED"

    def test_exact_dimension_boundary_float(self) -> None:
        assert sort(150.0, 10, 10, 5) == "SPECIAL"

    def test_very_heavy_not_bulky(self) -> None:
        assert sort(10, 10, 10, 100) == "SPECIAL"

    def test_combination_under_all_boundaries(self) -> None:
        assert sort(99, 99, 99, 19) == "STANDARD"
